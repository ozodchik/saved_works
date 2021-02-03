import requests
from bs4 import BeautifulSoup

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
        
