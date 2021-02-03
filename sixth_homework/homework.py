import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']


def parsing(args):
    posts_list = []
    keywords = args
    URL = "https://habr.com/ru/all/"
    response = requests.get(URL)
    parser = BeautifulSoup(response.text, "html.parser")
    all_posts = parser.find_all("article", class_="post post_preview")
    for previews in all_posts:
        hubs = previews.find_all("ul", class_="post__hubs inline-list")
        hub = list(map(lambda hub: hub.text.strip().lower(), hubs))
        for hub_text in hub:
            if any((d_h in hub_text for d_h in keywords)):
                post = previews.find("a", class_="post__title_link")
                time_post = previews.find("span", class_="post__time")
                for name in post:
                    posts_name = name

                for time in time_post:
                    posts_time = time

                posts_link = post["href"]

                posts_list.append(f"{posts_time} - {posts_name} - {posts_link}")
    return posts_list


if __name__ == "__main__":
    print(parsing(KEYWORDS))
