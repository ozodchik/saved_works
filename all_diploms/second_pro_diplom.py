import requests
from urllib.parse import urlencode, urljoin
import json
from bs4 import BeautifulSoup

# APP_ID = 7637207
# OAUTH_URL = "https://oauth.vk.com/authorize"
# REDIRECT_URI = "https://oauth.vk.com/blank.html"
# SCOPE = "status"
# OAUTH_PARAMS ={
#     "redirect_uri": REDIRECT_URI,
#     "scope": SCOPE,
#     "response_type": "token",
#     "client_id": APP_ID
# }
# print('?'.join([OAUTH_URL, urlencode(OAUTH_PARAMS)]))
# TOKEN = "3aafa9d63bac70459322e19019620aa0186310b0c302ec124430c482b0885d33e166be7be9d5890b60694"
# API_BASE_URL = "https://api.vk.com/method/"
# User_ID = 616586034
# V = "5.89"


# def info_celtics_wiki():
#     content = "https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D1%81%D1%82%D0%BE%D0%BD_%D0%A1%D0%B5%D0%BB%D1%82%D0%B8%D0%BA%D1%81"
#     response = f"Ссылка на статью про Boston_Celtics с Википедии:\n{content}"
#     return response
#
#
# def news_celtics():
#     response = requests.get("https://www.sports.ru/boston-celtics/")
#     parser = BeautifulSoup(response.text, "html.parser")
#     res = parser.find_all("div", class_="nl-item")
#     some_list = []
#     for i in res:
#         article = i.find_all("a", class_="short-text")
#         for news in article:
#             link = news["href"]
#             for name in news:
#                 description = name
#                 some_list.append(f"Название: {description} -> Ссылка: {link}")
#     return some_list
#
#
# def search_users():
#     API_BASE_URL = "https://api.vk.com/method/"
#     link = urljoin(API_BASE_URL, "users.search")
#     response = requests.get(link,
#                             params={
#                                 "access_token": TOKEN,
#                                 "age_from": "18",
#                                 "sex": "0",
#                                 "status": "1",
#                                 "v": V,
#                                 "is_closed": False,
#                                 "can_access_closed": True,
#                                 "fields": ['city']
#                             })
#     response_json = response.json()["response"]["items"]
#     for i in response_json:
#         print(i)
#
#
# def choose_biggest_size(sizes):
#     SIZES = "smxopqryzw"
#     return max(sizes, key=lambda s: SIZES.index(s["type"]))
#
#
# def get_photos():
#     API_BASE_URL = "https://api.vk.com/method/"
#     link = urljoin(API_BASE_URL, "photos.get")
#     res = requests.get(
#         link,
#         params={
#             "access_token": TOKEN,
#             "v": V,
#             "album_id": "profile",
#             "extended": 1,
#             "owner_id": User_ID,
#             "photo_sizes": 1,
#         },
#     )
#     res_json = res.json()["response"]["items"]
#     link_list = []
#     for photo in res_json:
#         count_like = photo["likes"]["count"]
#         biggest_size = choose_biggest_size(photo["sizes"])
    #     new_dict = {
    #         "ID Фото": photo["id"],
    #         "наибольший размер": biggest_size,
    #     }
    #     link_list.append(new_dict)
    # return (
    #     f"Топ 3 фото с самым большим размером : \n {link_list} \n"
    # )


# print(get_photos())
