import random

import requests
import time
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import lxml
import json
from reviews import reviews_parser
# from write_wp import write_in_wp
import re




def pars(url, connection):
    url = f"{url.removesuffix('/location')}?languages=all"
    headers = {
        "User-Agent": generate_user_agent()
    }
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        pass
    else:
        print(f"{url} ничего не найдено {r.status_code}")
        return
    html_cod = r.text
    soup = BeautifulSoup(html_cod, "lxml")
    script_1 = soup.find("script", type="application/ld+json").text
    script_2 = soup.find("script", type="application/json").text
    js_1 = json.loads(script_1)
    js_2 = json.loads(script_2)

    url_offer_logo = soup.find("img", class_="business-profile-image_image__jCBDc").attrs['src']
    name_img = url.split('?')[0].split('/')[-1].replace('.', '_') + '.png'
    img_logo = requests.get(url=url_offer_logo, headers=headers)
    if img_logo.status_code == 200:
        with open(f'data/logo/{name_img}', 'wb') as logo:
            while True:
                chunk = img_logo.content.read(1024)
                if not chunk:
                    break
                logo.write(chunk)
        offer_logo = True
    else:
        offer_logo = False

    if offer_logo == False:
        print(f"{url} без лого, пропускаю")
        return
    for i, offer_type in enumerate(js_1['@graph']):
        if offer_type['@type'] == 'LocalBusiness':
            index_LocalBusiness = i
            break

    offer_name = js_1['@graph'][index_LocalBusiness]['name']
    try:
        offer_description = js_1['@graph'][index_LocalBusiness]['description']
    except KeyError:
        offer_description = "No description"
    offer_url = js_1['@graph'][index_LocalBusiness]['sameAs']

    try:
        offer_email = js_1['@graph'][index_LocalBusiness]['email']
    except KeyError:
        offer_email = "No email"

    try:
        offer_address = js_1['@graph'][index_LocalBusiness]['address']
    except KeyError:
        offer_address = "No address"

    if offer_email == "No email" and offer_address == "No address" and offer_description == "No description":
        print(f"{url} Нет почты, адреса и описания. Пропускаю")
        return

    block_content = soup.find("div", class_="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_sideColumnCard__eyHWa")

    elements = block_content.findAll("div", class_="card_cardContent__sFUOe styles_cardContent__sQHcU")
    find_element = re.compile('.*'.join(re.escape('Category')))
    for element in elements:
        if find_element.search(str(element)):
            del_element_category = element
    del_element_category.decompose()
    try:
        block_content.find("p", class_="typography_body-s__aY15Q typography_appearance-subtle__8_H2l styles_descriptionSubHeadline__opTat").decompose()
    except:
        pass
    # block_Visit_this_website = soup.find("div", class_="styles_badgesWrapper__6VasU")
    try:
        offer_rating = js_1['@graph'][index_LocalBusiness]['aggregateRating']['ratingValue']
    except:
        offer_rating = soup.find("p", class_="typography_body-l__KUYFJ typography_appearance-subtle__8_H2l").text
    # verified = soup.find("div", class_="typography_body-xs__FxlLP typography_appearance-default__AAY17 typography_weight-heavy__E1LTj styles_verificationIcon___X7KO").text
    verified_company = js_2['props']['translations']['business-profile-page/header/business-information/verified-company']
    if verified_company == 'VERIFIED COMPANY':
        verified = 1
    else:
        verified = 0

    category_list = []
    count_itemListElement = len(js_1['@graph'][4]['itemListElement'])

    for i in range(1, count_itemListElement - 1):
        category_list.append(js_1['@graph'][4]['itemListElement'][i]['name'])

    reviews_list = []
    parser_reviews_stop = random.randint(100, 230)
    # print(f"коментов {parser_reviews_stop}")
    script_reviews = soup.find("script", id="__NEXT_DATA__").text
    js_reviews = json.loads(script_reviews)
    numberOfReviews = js_reviews['props']['pageProps']['businessUnit']['numberOfReviews']
    reviews = js_reviews['props']['pageProps']['reviews']
    reviews_parser(reviews, reviews_list, numberOfReviews, parser_reviews_stop)
    if numberOfReviews > 20:
        page = 2
        flag = True

        while flag == True:
            url_review = f"{url}&page={page}"
            r = requests.get(url=url_review)
            if r.status_code == 200:
                html_cod = r.text
                soup = BeautifulSoup(html_cod, "lxml")
                script_reviews = soup.find("script", id="__NEXT_DATA__").text
                js_reviews = json.loads(script_reviews)
                reviews = js_reviews['props']['pageProps']['reviews']
                page += 1
                flag = reviews_parser(reviews, reviews_list, numberOfReviews, parser_reviews_stop)
            else:
                print(f"ошибка запроса{r.status_code}. Пауза 5 сек.")
                time.sleep(5)

    else:
        url_review = f"{url}&page=1"


    dict_content = {
        'block_content': str(block_content),
        # 'block_Visit_this_website': str(block_Visit_this_website),
        'offer_name': offer_name,
        'verified': verified,
        'offer_description': offer_description,
        'offer_url': offer_url,
        'offer_logo': offer_logo,
        'offer_email': offer_email,
        'offer_address': offer_address,
        'offer_rating': offer_rating,
        'category_list': category_list,
        'reviews_list': reviews_list
    }
    with open('dict_content.json', 'w') as f:
        json.dump(dict_content, f)
    # print('1')

    print(f"{url} спарсил")
    write_in_wp(dict_content, connection)
    print(f"{url} записал в wp")



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