import vk_api
from random import randrange
import time
import requests
from urllib.parse import urljoin
from vk_api.longpoll import VkLongPoll, VkEventType
from pro_diplom.config_keys import user_token as u_t, bots_token as b_t
from pro_diplom.need_functions_modules import info_celtics_wiki as i_s_w, news_celtics as n_c, know_username, get_photos
from pro_diplom.need_functions_modules import search_users

STATUSES = dict(hello=0, commands=1, choose_gender=2, choose_country=3, choose_city=4,
                choose_age_from=5, choose_age_to=6, choose_status=7, news=8, history=9)

COMMANDS = {
    "quit": "выход",
    "new_search": "new search",
    "choose_search": "search_users",
    "choose_news": "news",
    "choose_history_team": "history",
    "gender_man": "мужчина",
    "gender_woman": "женщина",
    "any": "неважно",
    "liked": "лайкнутые"}


class ServerBot:
    def __init__(self, users_token=u_t, group_token=b_t):
        self.vk = vk_api.VkApi(token=group_token)
        self.long_poll = VkLongPoll(self.vk)
        self.users_token = users_token
        self.request = ''
        self.user_id = 0
        self.state = STATUSES["hello"]
        self.commands_dict = COMMANDS
        self.gender = None
        self.age_from = 0
        self.age_to = 0
        self.country = "Россия"
        self.town = "москва"

    def send_msg(self, user_id, message):
        self.vk.method("messages.send", {'user_id': user_id, 'message': message, "random_id": randrange(10 ** 7)})

    def hello(self):
        if self.request == "привет" and self.state == STATUSES["hello"]:
            self.send_msg(self.user_id, f"Привет {know_username(self.user_id)}!\n"
                                        f"Я бот VKinder ваш помощник для помощи вводите bot_commands")
            self.state = STATUSES["hello"]
            return self.state
        else:
            self.send_msg(self.user_id, self.send_msg(self.user_id, f"Произошла ошибка! вы ввели не правильную команду!"
                                                      f"поэтому мы возвращаемся в состояние bot_commands"))
            self.commands()

    def commands(self):
        self.send_msg(self.user_id,
                      f"Выберите команду:\n"
                      f"Search_users: Искать людей для знакомства\n"
                      f"News: Новости про команды Boston Celtics\n"
                      f"History: История команды Boston Celtics и прочие материалы\n")
        if self.request == "search_users":
            self.state = STATUSES["commands"]
            return self.state

        elif self.request == "news":
            self.state = STATUSES["news"]
            return self.state

        elif self.request == "history":
            self.state = STATUSES["history"]
            return self.state

        else:
            self.state = STATUSES["commands"]
            return self.state

    def search_country(self):
        self.send_msg(self.user_id, f"Вводите страну поиска\n")
        self.state = STATUSES["choose_country"]
        self.country = self.request
        return self.state

    def input_town(self):
        self.send_msg(self.user_id, f"Вводите город поиска\n")
        self.state = STATUSES["choose_city"]
        self.town = self.request

    def news(self):
        self.send_msg(self.user_id, n_c())
        self.state = STATUSES["commands"]

    def history(self):
        self.send_msg(self.user_id, i_s_w())
        self.state = STATUSES["commands"]

    def talking(self):
        for event in self.long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    self.request = event.text.lower()
                    self.user_id = event.user_id
                    if self.request == "привет" and self.state == STATUSES["hello"]:
                        self.hello()

                    elif self.request == "bot_commands":
                        self.commands()

                    elif self.request == "search_users":
                        self.search_country()
                        self.state = STATUSES["choose_country"]

                    elif self.state == STATUSES["choose_country"]:
                        pass

                    elif self.request == "news":
                        for news_info in n_c():
                            self.send_msg(self.user_id, news_info)
                        self.send_msg(self.user_id, "Этот сеанс окончен и мы возвращаемся в состояние bot_commands")
                        self.commands()

                    elif self.request == "history":
                        self.send_msg(self.user_id, i_s_w())
                        self.send_msg(self.user_id, "Этот сеанс окончен и мы возвращаемся в состояние bot_commands")
                        self.commands()

                    else:
                        self.send_msg(self.user_id, f"Произошла ошибка! вы ввели не правильную команду!\n"
                                                    f"Поэтому мы возвращаемся в состояние bot_commands\n")
                        self.commands()


if __name__ == "__main__":
    some_user = ServerBot(u_t, b_t)
    some_user.talking()
