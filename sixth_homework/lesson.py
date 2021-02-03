import requests
from bs4 import BeautifulSoup


# category_hubs = ["программирование", "agile", "cms"]
# ok = requests.get("https://habr.com/ru/all/")
# parsing = BeautifulSoup(ok.text, "html.parser")
# posts = parsing.find_all("article", class_="post")
# for a in posts:
#     hubs = a.find_all("li", class_="inline-list__item_hub")
#     r = list(map(lambda hub: hub.text.strip().lower(), hubs))
#     for hub_text in r:
#         if any((dh in hub_text for dh in category_hubs)):
#             data = a.find("span", class_="post__time").text.strip()
#             link = a.find("a", class_="post__title_link")
#             link_link = link.attrs.get("href")
#             link_text = link.text.strip()
#             print(data, link_link, link_text)
#             break



response = requests.get("https://habr.com/ru/all")
parser = BeautifulSoup(response.text, "html.parser")
posts = parser.find_all("article", class_="post post_preview")
for post in posts:
    hubs = post.find_all("li", class_="inline-list__item inline-list__item_hub")
    hubs_list = []
    for hub in hubs:
        hubs_list.append(hub.text.strip().lower().strip(","))

    for i in hubs_list:
        name = post.find("a", class_="post__title_link")
        link = name.attrs.get("href")
        link_name = name.text.strip()
        print(link_name, link)
        break
