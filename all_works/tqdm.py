import speech_recognition as s_r
import pyttsx3
import sys
import requests
from bs4 import BeautifulSoup


def talk_alita(talk):
    engine = pyttsx3.init()
    engine.say(talk)
    engine.runAndWait()


talk_alita("привет босс!  я готова к работы и жду приказов")


def command():
    r = s_r.Recognizer()

    with s_r.Microphone(device_index=1) as source:
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print(f"[log] я слышу: {task}")
        talk_alita(f"я слышу:{task}")

    except:
        talk_alita("я не слышу вас.. пожалуйста повторите команду!")
        task = command()

    return task


def working(task):
    if "привет" == task:
        talk_alita("привет босс. как вы.  как жизнь?!  не болеете?!")

    elif "стоп" == task:
        talk_alita("отключаюсь! хорошего дня босс!")
        sys.exit()

    elif "открой папку" == task:
        talk_alita("открываю папку")
        with open("file.txt", "w", encoding="utf-8") as f:
            f.write("hello world!")
        talk_alita("сеанс завершён!")

    elif "анекдот" == task:
        talk_alita("хах. анекдотов у меня нет. но могу рассказать что то в этом духе.  так вот  жена сказала.  лучше бы  я вышла за \
        чёрта! а муж говорит  на родственниках не женится!!! ахахахах типа смешно  да?!")

    elif "скрапинг" == task:
        talk_alita("а какие сайты вы хотите парсить?")
        talk_alita("на выбор есть хабр  хитмо  емпатрик.net")
        talk_alita(
            "на хабре можно парсить статьи  а на хитмо любую  музыку   а на емпатрик  музыки мияги тоже можно парсить!")

        if ("мияги" or "miyagi") or ("емпатрик" or "empatrick") in task:

            talk_alita("команда принята!  будем парсить сайт с музыками мияги")
            response = requests.get("https://mp3uk.net/pesen-2020/6956-miyagi-andy-panda-yamakasi-novyj-albom.html")
            parser = BeautifulSoup(response.text, "html.parser")
            musics_links = parser.find_all("div", class_="track-item fx-row fx-middle js-item")
            for name in musics_links:
                music_name = name.find_all("div", class_="track-title nowrap")
                links = name.find_all("a", class_="track-dl")
                musics_dict = {}
                for origin_name in music_name:
                    for i in origin_name:
                        names_music = i

                for link in links:
                    all_links = link["href"]
                    musics_dict[names_music] = "https:" + all_links

                for music, link_music in musics_dict.items():
                    print(f"{music}-{link_music}")
            talk_alita("парсинг завершён наверху все ссылки на скачивания!")

        elif "хабр" or "habr" == task:
            talk_alita("начался процесс парсинга хабра")
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
            talk_alita("процесс парсинга завершён! наверху ссылки на статьи!")

        elif "хитмо" or "hitmo" == task:
            talk_alita("процесс парсинга  сайта хитмо началось!")
            response = requests.get("https://hotmo.org/songs/top-today")
            parser = BeautifulSoup(response.text, "html.parser")
            names_links = parser.find_all("div", class_="track__info")
            music_list = {}
            for names in names_links:
                track_title = names.find_all("div", class_="track__title")
                track_link = names.find_all("a", class_="track__download-btn")
                for all_tracks in track_title:
                    for i in all_tracks:
                        my_track = i.strip()

                for all_links in track_link:
                    link = all_links["href"]
                    music_list[my_track] = link

            for music, links in music_list.items():
                print(f"{music}-{links}")

            talk_alita("процесс парсинга сайта хитмо завершён")


while True:
    working(command())
