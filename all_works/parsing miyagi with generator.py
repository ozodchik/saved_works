import requests
from bs4 import BeautifulSoup

response = requests.get("https://mp3uk.net/pesen-2020/6956-miyagi-andy-panda-yamakasi-novyj-albom.html")
parser = BeautifulSoup(response.text, "html.parser")
musics_links = parser.find_all("div", class_="track-item fx-row fx-middle js-item")


def get_track():
    track_dict = {}
    music_links = parser.find_all("div", class_="track-item fx-row fx-middle js-item")
    for names in music_links:
        track_name = [names.find_all("div", class_="track-title nowrap") for name in names]
        track_link = [names.find_all("a", class_="track-dl") for name in names]
        for tracks_info in track_name:
            for info in tracks_info:
                for tracks in info:
                    music_name = tracks
        for links in track_link:
            for link in links:
                download_link = "https:" + link["href"]
                track_dict[music_name] = download_link

    for singers, musics in track_dict.items():
        print(f"{singers} - {musics}")
    return "End program!"


print(get_track())
