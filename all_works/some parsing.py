import requests
from bs4 import BeautifulSoup

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


