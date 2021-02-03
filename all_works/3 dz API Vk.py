from urllib.parse import urljoin
import requests


TOKEN = "здесь токен вк"
V = "5.214"
API_BASE_URL = "https://api.vk.com/method/"
cl_id = 56428622 # какой то айди

class User:
    def __init__(self, token=TOKEN, version=V, client_id=cl_id):
        self.token = token
        self.version = version
        self.client_id = client_id

    def __str__(self):
        return f"ссылка на ваш профиль: https://vk.com/id{cl_id}"

    def get_user_friends(self):
        link = urljoin(API_BASE_URL, "friends.get")
        res = requests.get(link, params={"access_token": self.token, "v": self.version})
        if res.status_code == 200:
            return f" Всё прошло успешно! \n Статус кода: {res.status_code} \n ваши друзья: {res.json()}"
        else:
            return f"Произошла ошибка! \n Код ошибки: {res.status_code}"


if __name__ == "__main__":
    first = User(TOKEN, V, cl_id)
    print(first.get_user_friends())
    print(first)