from urllib.parse import urljoin
import requests


TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"
V = "5.214"
API_BASE_URL = "https://api.vk.com/method/"


class User:
    BASE_URL = API_BASE_URL

    def __init__(self, token=TOKEN, version=V):
        self.token = token
        self.version = version

    def get_user_friends(self):
        link = urljoin(API_BASE_URL, "friends.get")
        order = "name"
        res = requests.get(link, params={"access_token": self.token, "v": self.version})
        if res.status_code == 200:
            return f" Всё прошло успешно! \n Статус кода: {res.status_code} \n ваши друзья: {res.json()}"
        else:
            return f"Произошла ошибка! \n Код ошибки: {res.status_code}"


if __name__ == "__main__":
    first = User(TOKEN, V)
    print(first.get_user_friends())
    print(first)