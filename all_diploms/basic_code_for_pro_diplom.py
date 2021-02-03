from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from pro_diplom.need_functions_modules import info_celtics_wiki as i_s_w
from pro_diplom.need_functions_modules import news_celtics as n_c
BOT_token = "ed8e88703b96c5fd0b77dbb37fe2d76113a49ccfd7639d66214da340a22d98741185dad363f6d79661da8"
vk = vk_api.VkApi(token=BOT_token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text.lower()

            if request == "привет":
                write_msg(event.user_id, f"Привет, пользователь с ID: {event.user_id} \n Я 'VKinder' ваш бот-помощник! "
                                         f"Если нужна помощь то можете писать: Bot command и я вам помогу!")

            elif request == "bot command":
                write_msg(event.user_id, f"Все команды для бота:\n 1)Поиск пользователей ВК \n "
                                         f"2)Информация про Boston Celtics (история и т.д.) \n"
                                         f"3)Новости про Boston Celtics \n"
                                         f"Вводите номер команды")

            elif request == "1":
                write_msg(event.user_id, "Вводите параметры:")
                write_msg(event.user_id, f"Метод age_from -> Возраст от ...\n"
                                         f"Метод age_to -> Возраст до ...\n"
                                         f"Метод person_pol -> Man: Мужчина, Woman: Женьщина, Any: Любой"
                                         f"")

            elif request == "2":
                write_msg(event.user_id, i_s_w())

            elif request == "3":
                write_msg(event.user_id, "Все новости и статьи: \n")
                for i in n_c():
                    write_msg(event.user_id, i)

            elif request == "пока":
                write_msg(event.user_id, "Пока((")

            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")



# token = input('Token: ')
#
# vk = vk_api.VkApi(token=token)
# longpoll = VkLongPoll(vk)
#
#
# def write_msg(user_id, message):
#     vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7), })
#
#
# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW:
#
#         if event.to_me:
#             request = event.text
#
#             if request == "привет":
#                 write_msg(event.user_id, f"Хай, {event.user_id}")
#             elif request == "пока":
#                 write_msg(event.user_id, "Пока((")
#             else:
#                 write_msg(event.user_id, "Не поняла вашего ответа...")
#
#
# if __name__ == "__main__":
#     write_msg(616586034, "helloo")



