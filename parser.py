import asyncio
from asyncio import Semaphore
import aiohttp
from bs4 import BeautifulSoup
import lxml
from user_agent import generate_user_agent
import random
import re
import time
import json
import requests
import os
import pathlib
# from data.variables import *
from reviews import reviews_parser

list_threads = []


async def parser_url(url, session, semaphore):
    await semaphore.acquire()

    # list_threads[index]["id"] = index
    url = f"{url.removesuffix('/location')}?languages=all"
    headers = {
        "User-Agent": generate_user_agent()
    }
    async with session.get(url=url, headers=headers) as r:
        if r.status == 200:
            pass
        else:
            print(f"{url} ответ сервера {r.status}")
            return
        html_cod = await r.text()
        soup = BeautifulSoup(html_cod, "lxml")
        script_1 = soup.find("script", type="application/ld+json").text
        script_2 = soup.find("script", type="application/json").text
        js_1 = json.loads(script_1)
        js_2 = json.loads(script_2)

        url_offer_logo = soup.find("img", class_="business-profile-image_image__jCBDc").attrs['src']
        name_img = url.split('?')[0].split('/')[-1].replace('.','_') + '.png'
        async with session.get(url=url_offer_logo, headers=headers) as img_logo:
        # img_logo = requests.get(url_offer_logo)
            if img_logo.status == 200:
                with open(f'data/logo/{name_img}', 'wb') as logo:
                    while True:
                        chunk = await img_logo.content.read(1024)
                        if not chunk:
                            break
                        logo.write(chunk)
                    # logo.write(img_logo.content.read(1024))
                offer_logo = True
            else:
                offer_logo = False
            if offer_logo == False:
                # print(f"{url} без лого, пропускаю")
                return

        for i, offer_type in enumerate(js_1['@graph']):
            if offer_type['@type'] == 'LocalBusiness':
                index_LocalBusiness = i
                break
        offer_name = js_1['@graph'][index_LocalBusiness]['name']
        # list_threads[index] = {'offer_name':offer_name}
        # list_threads[index]["offer_name"] = offer_name

        try:
            offer_description = js_1['@graph'][index_LocalBusiness]['description']
            # list_threads[index]["offer_description"] = offer_description
        except KeyError:
            offer_description = "No description"

        offer_url = js_1['@graph'][index_LocalBusiness]['sameAs']
        # list_threads[index]["offer_url"] = offer_url

        try:
            offer_email = js_1['@graph'][index_LocalBusiness]['email']
            # list_threads[index]["offer_email"] = offer_email
        except KeyError:
            offer_email = "No email"

        try:
            offer_address = js_1['@graph'][index_LocalBusiness]['address']
            # list_threads[index]["offer_address"] = offer_address
        except KeyError:
            offer_address = "No address"
        # list_threads[index] = {'offer_address': offer_address}

        if offer_email == "No email" and offer_address == "No address" and offer_description == "No description":
            # print(f"{url} Нет почты, адреса и описания. Пропускаю")
            return

        list_threads.append({"url": url})
        index = len(list_threads) - 1

        list_threads[index]["offer_name"] = offer_name
        list_threads[index]["operation"] = "Название"
        list_threads[index]["offer_description"] = offer_description
        list_threads[index]["operation"] = "Описание"
        list_threads[index]["offer_url"] = offer_url
        list_threads[index]["operation"] = "Ссылка"
        list_threads[index]["offer_email"] = offer_email
        list_threads[index]["operation"] = "email"
        list_threads[index]["offer_address"] = offer_address
        list_threads[index]["operation"] = "Адрес"

        block_content = soup.find("div",
                                  class_="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_sideColumnCard__eyHWa")

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
        list_threads[index]["block_content"] = block_content
        list_threads[index]["operation"] = "block_content"

        # block_Visit_this_website = soup.find("div", class_="styles_badgesWrapper__6VasU")
        try:
            offer_rating = js_1['@graph'][index_LocalBusiness]['aggregateRating']['ratingValue']
        except:
            offer_rating = soup.find("p", class_="typography_body-l__KUYFJ typography_appearance-subtle__8_H2l").text
        # list_threads[index] = {'offer_rating': offer_rating}
        list_threads[index]["offer_rating"] = offer_rating
        list_threads[index]["operation"] = "Рейтинг"

        verified_company = js_2['props']['translations'][
            'business-profile-page/header/business-information/verified-company']
        if verified_company == 'VERIFIED COMPANY':
            verified = 1
        else:
            verified = 0
        list_threads[index]["verified"] = verified
        list_threads[index]["operation"] = "Верификация"

        category_list = []
        count_itemListElement = len(js_1['@graph'][4]['itemListElement'])
        for i in range(1, count_itemListElement - 1):
            category_list.append(js_1['@graph'][4]['itemListElement'][i]['name'])
        # list_threads[index] = {'category_list': category_list}
        list_threads[index]["category_list"] = category_list
        list_threads[index]["operation"] = "Категории"

        # list_threads[index]["operation"] = "Начинаю парсинг отзывов"
        # reviews_list = []
        # parser_reviews_stop = random.randint(100, 230)
        # # print(f"коментов {parser_reviews_stop}")
        # script_reviews = soup.find("script", id="__NEXT_DATA__").text
        # js_reviews = json.loads(script_reviews)
        # numberOfReviews = js_reviews['props']['pageProps']['businessUnit']['numberOfReviews']
        # reviews = js_reviews['props']['pageProps']['reviews']
        # reviews_parser(reviews, reviews_list, numberOfReviews, parser_reviews_stop)
        # if numberOfReviews > 20:
        #     page = 2
        #     flag = True
        #
        #     while flag == True:
        #         url_review = f"{url}&page={page}"
        #         r = requests.get(url=url_review)
        #         if r.status_code == 200:
        #             html_cod = r.text
        #             soup = BeautifulSoup(html_cod, "lxml")
        #             script_reviews = soup.find("script", id="__NEXT_DATA__").text
        #             js_reviews = json.loads(script_reviews)
        #             reviews = js_reviews['props']['pageProps']['reviews']
        #             page += 1
        #             flag = reviews_parser(reviews, reviews_list, numberOfReviews, parser_reviews_stop)
        #         else:
        #             print(f"ошибка запроса{r.status_code}. Пауза 5 сек.")
        #             time.sleep(5)
        #
        # else:
        #     url_review = f"{url}&page=1"
        # list_threads[index]["reviews_list"] = reviews_list
        # list_threads[index]["operation"] = "Парсинг закончен"

        logo = pathlib.path(f"data/logo/{name_img}")
        logo.unlink()
        # os.ulink(f"data/logo/{name_img}")
        list_threads.pop(index)  # удаляет элемент из списка

        # dict_content = {
        #     'block_content': str(block_content),
        #     # 'block_Visit_this_website': str(block_Visit_this_website),
        #     'offer_name': offer_name,
        #     'verified': verified,
        #     'offer_description': offer_description,
        #     'offer_url': offer_url,
        #     'offer_logo': offer_logo,
        #     'offer_email': offer_email,
        #     'offer_address': offer_address,
        #     'offer_rating': offer_rating,
        #     'category_list': category_list,
        #     'reviews_list': reviews_list
        # }
        # with open('list_threads.json', 'w') as f:
        #     json.dump(list_threads, f)
        # print(list_threads)

        # print(f"{url} спарсил")
        # write_in_wp(dict_content, connection)
        # print(f"{url} записал в wp")

    semaphore.release()

async def gahter():
    with open('data/trustpilot.txt','r', encoding='utf-8') as f_read:
        url_list = f_read.read().split('\n')
    if len(url_list) > 0:
        semaphore = Semaphore(30)
        tasks = []
    else:
        print("ссылки закончились")

    async with aiohttp.ClientSession() as session:
        for url in url_list[10:110]:
            # print(f"ссылка {url}")
            # print(f"сессия {session}")
            # print(f"семафор {semaphore}")
            task = asyncio.create_task(parser_url(url, session, semaphore))
            tasks.append(task)
        await asyncio.gather(*tasks)

def test_func():
    print("тестовая функция")

if __name__ == '__main__':
    # asyncio.run(gahter())
    asyncio.get_event_loop().run_until_complete(gahter())
    print(list_threads)
