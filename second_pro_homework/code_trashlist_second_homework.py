import requests
from urllib.parse import urljoin
#
#
# class Iterable:
#
#     def __init__(self, url):
#         self.url = url
#
#     def get_responses(self):
#         get_response = requests.get(self.url)
#         response_json = get_response.json()
#         for names in response_json:
#             country = names["name"]["common"].replace(" ", "_")
#             print(country)
#             urls = urljoin("https://en.wikipedia.org/wiki/", country)
#             print(urls)
#
#
# if __name__ == "__main__":
#     a = Iterable("https://raw.githubusercontent.com/mledoze/countries/master/countries.json")
#     print(a.get_responses())





# def Download(url):
#     response = requests.get(url)
#     res = response.json()
#     for name in res:
#         name_country = name["name"]["common"]
#         print(name_country)
#     return
#
# if __name__ == "__main__":
#     result = Download("https://raw.githubusercontent.com/mledoze/countries/master/countries.json")
#     print(result)

class Iterable:
    def __init__(self, url):
        self.get_response = requests.get(url)
        self.response_json = self.get_response.json()
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration


if __name__ == "__main__":
    with open("file.txt", "w", encoding="UTF-8") as f:
        a = Iterable("https://raw.githubusercontent.com/mledoze/countries/master/countries.json")
        for names in a.response_json:
            country = names["name"]["common"].replace(" ", "_")
            urls = urljoin("https://en.wikipedia.org/wiki/", country)
            f.write(f'{country}-{urls} \n')

