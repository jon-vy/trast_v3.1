import random

import requests
import time
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import lxml
import json
from PySide6.QtCore import Slot, Signal, QObject
from reviews import reviews_parser
# from write_wp import write_in_wp
import re



class Signals(QObject):
    signal_progress_update = Signal(list)

class Parser():
    def __init__(self, url):
        super().__init__()
        self.url = f"{url.removesuffix('/location')}?languages=all"
        self.headers = None

    def pars(self):  #, connection
        # url = f"{url.removesuffix('/location')}?languages=all"
        # print(url)
        self.headers = {
            "User-Agent": generate_user_agent()
        }
        self.r = requests.get(url=self.url, headers=self.headers)
        if self.r.status_code == 200:
            pass
        else:
            # print(f"{url} ничего не найдено {r.status_code}")
            return
        self.html_cod = self.r.text
        self.soup = BeautifulSoup(self.html_cod, "lxml")
        self.script_1 = self.soup.find("script", type="application/ld+json").text
        self.script_2 = self.soup.find("script", type="application/json").text
        self.js_1 = json.loads(self.script_1)
        self.js_2 = json.loads(self.script_2)

        self.url_offer_logo = self.soup.find("img", class_="business-profile-image_image__jCBDc").attrs['src']
        self.name_img = self.url.split('?')[0].split('/')[-1].replace('.', '_') + '.png'
        self.img_logo = requests.get(url=self.url_offer_logo, headers=self.headers)
        if self.img_logo.status_code == 200:
            with open(f'data/logo/{self.name_img}', 'wb') as self.logo:
                for chunk in self.img_logo.iter_content(chunk_size=1024):
                    self.logo.write(chunk)
            self.offer_logo = True
        else:
            self.offer_logo = False

        if self.offer_logo == False:
            print(f"{self.url} без лого, пропускаю")
            return
        for i, offer_type in enumerate(self.js_1['@graph']):
            if offer_type['@type'] == 'LocalBusiness':
                self.index_LocalBusiness = i
                break

        self.offer_name = self.js_1['@graph'][self.index_LocalBusiness]['name']
        try:
            offer_description = self.js_1['@graph'][self.index_LocalBusiness]['description']
        except KeyError:
            self.offer_description = "No description"
        self.offer_url = self.js_1['@graph'][self.index_LocalBusiness]['sameAs']

        try:
            self.offer_email = self.js_1['@graph'][self.index_LocalBusiness]['email']
        except KeyError:
            self.offer_email = "No email"

        try:
            self.offer_address = self.js_1['@graph'][self.index_LocalBusiness]['address']
        except KeyError:
            self.offer_address = "No address"

        if self.offer_email == "No email" and self.offer_address == "No address" and self.offer_description == "No description":
            print(f"{self.url} Нет почты, адреса и описания. Пропускаю")
            return

        self.block_content = self.soup.find("div", class_="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_sideColumnCard__eyHWa")

        self.elements = self.block_content.findAll("div", class_="card_cardContent__sFUOe styles_cardContent__sQHcU")
        self.find_element = re.compile('.*'.join(re.escape('Category')))
        for element in self.elements:
            if self.find_element.search(str(element)):
                self.del_element_category = self.element
        self.del_element_category.decompose()
        try:
            self.block_content.find("p", class_="typography_body-s__aY15Q typography_appearance-subtle__8_H2l styles_descriptionSubHeadline__opTat").decompose()
        except:
            pass
        # block_Visit_this_website = soup.find("div", class_="styles_badgesWrapper__6VasU")
        try:
            self.offer_rating = self.js_1['@graph'][self.index_LocalBusiness]['aggregateRating']['ratingValue']
        except:
            self.offer_rating = self.soup.find("p", class_="typography_body-l__KUYFJ typography_appearance-subtle__8_H2l").text
        # verified = soup.find("div", class_="typography_body-xs__FxlLP typography_appearance-default__AAY17 typography_weight-heavy__E1LTj styles_verificationIcon___X7KO").text
        self.verified_company = self.js_2['props']['translations']['business-profile-page/header/business-information/verified-company']
        if self.verified_company == 'VERIFIED COMPANY':
            self.verified = 1
        else:
            self.verified = 0

        self.category_list = []
        self.count_itemListElement = len(self.js_1['@graph'][4]['itemListElement'])

        for i in range(1, self.count_itemListElement - 1):
            self.category_list.append(self.js_1['@graph'][4]['itemListElement'][i]['name'])

        self.reviews_list = []
        self.parser_reviews_stop = random.randint(100, 230)
        # print(f"коментов {parser_reviews_stop}")
        self.script_reviews = self.soup.find("script", id="__NEXT_DATA__").text
        self.js_reviews = json.loads(self.script_reviews)
        self.numberOfReviews = self.js_reviews['props']['pageProps']['businessUnit']['numberOfReviews']
        self.reviews = self.js_reviews['props']['pageProps']['reviews']
        self.reviews_parser(self.reviews, rself.eviews_list, self.numberOfReviews, self.parser_reviews_stop)
        if self.numberOfReviews > 20:
            self.page = 2
            self.flag = True

            while self.flag == True:
                self.url_review = f"{self.url}&page={self.page}"
                self.r = requests.get(url=self.url_review)
                if self.r.status_code == 200:
                    self.html_cod = self.r.text
                    self.soup = BeautifulSoup(self.html_cod, "lxml")
                    self.script_reviews = self.soup.find("script", id="__NEXT_DATA__").text
                    self.js_reviews = json.loads(self.script_reviews)
                    self.reviews = self.js_reviews['props']['pageProps']['reviews']
                    self.page += 1
                    self.flag = self.reviews_parser(self.reviews, self.reviews_list, self.numberOfReviews, self.parser_reviews_stop)
                else:
                    print(f"ошибка запроса{self.r.status_code}. Пауза 5 сек.")
                    time.sleep(5)

        else:
            url_review = f"{self.url}&page=1"


        self.dict_content = {
            'block_content': str(self.block_content),
            # 'block_Visit_this_website': str(block_Visit_this_website),
            'offer_name': self.offer_name,
            'verified': self.verified,
            'offer_description': self.offer_description,
            'offer_url': self.offer_url,
            'offer_logo': self.offer_logo,
            'offer_email': self.offer_email,
            'offer_address': self.offer_address,
            'offer_rating': self.offer_rating,
            'category_list': self.category_list,
            'reviews_list': self.reviews_list
        }
        with open('dict_content.json', 'w') as f:
            json.dump(self.dict_content, f)
        # print('1')

        print(f"{self.url} спарсил")
        # write_in_wp(dict_content, connection)
        print(f"{self.url} записал в wp")



if __name__ == '__main__':
    import time
    from connect_db import db_connect
    start = time.time()
    connection = db_connect()

    # with open('trustpilot.txt', 'r', encoding="utf-8") as f:
    #     url_list = f.read().split('\n')
    # for url in url_list[0:1]:
    #     pars(url, connection)

    # url = "https://www.trustpilot.com/review/privatevpn.com"
    # url = "https://www.trustpilot.com/review/taxafyn.dk"
    # url = "https://www.trustpilot.com/review/soandmo.com"
    # url = "https://www.trustpilot.com/review/eset.com/uk"
    # url = "https://www.trustpilot.com/review/www.resolutionlaw.co.uk"
    url = "https://www.trustpilot.com/review/discountdumpsterco.com/location"
    pars(url, connection)
    total_time = time.time() - start
    print(f"время {total_time}")