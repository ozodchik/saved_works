from urllib.parse import urljoin
from third_pro_homeworks.decorators_homework import function_logger as f_l
import requests


TOKEN = "здесь токен с вк"
V = "5.214"
API_BASE_URL = "https://api.vk.com/method/"


class User:
    BASE_URL = API_BASE_URL

    def __init__(self, token=TOKEN, version=V):
        self.token = token
        self.version = version

    @f_l
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
