import random


def reviews_parser(reviews, reviews_list, numberOfReviews, parser_reviews_stop, flag = None):
    for review in reviews:
        review_id = review['id']
        review_title = review['title']
        review_text = review['text']
        review_rating = review['rating']
        review_autor = review['consumer']['displayName']
        review_id = {
            "review_title": review_title,
            "review_text": review_text,
            "review_rating": review_rating,
            "review_autor": review_autor
        }

        reviews_list.append(review_id)
        if len(reviews_list) == parser_reviews_stop or len(reviews_list) == numberOfReviews:
            flag = False
            break
        else:
            flag = True
    return flag
    # print('1')


if __name__ == '__main__':

    page = 1
    reviews_list = []
    flag = True
    while flag == True:
        # url_reviews = f"https://www.trustpilot.com/review/privatevpn.com?languages=all&page={page}"
        # url_reviews = f"https://www.trustpilot.com/review/soandmo.com?languages=all&page={page}"
        url_reviews = f"https://www.trustpilot.com/review/taxafyn.dk?languages=all&page={page}"
        flag = reviews_parser(url_reviews, reviews_list, flag)
        page+=1

    # print('1')