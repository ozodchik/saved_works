import requests

# my_list = [None, "ozod", 19, list()]
# for a in my_list:
#     print(a)
#
# iter_list = iter(my_list)
# item = next(iter_list)
# print(item)
# item = next(iter_list)
# print(item)
# item = next(iter_list)
# print(item)
# item = next(iter_list)
# print(item)

# class Iterable:
#     def __init__(self, start: int, end: int):
#         self.start = start-1
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         if self.start == self.end:
#             raise StopIteration
#         return self.start
# if __name__ == "__main__":
#     a = Iterable(1, 10)
#     for b in a:
#         print(b)

# class Downloader:
#
#     def __init__(self, url):
#         response = requests.get(url, stream=True)
#         self.response_lines = response.iter_lines()
#
#     def __iter__(self):
#         return self.response_lines
#
#
# if __name__ == "__main__":
#     with open("habr.html", "wb") as file:
#         a = Downloader("http://habr.com")
#         for lines in a:
#             file.write(lines)

# def my_exp(start, end):
#     while start < end:
#         yield start
#         start += 1
#
# result = my_exp(1, 10)
# for res in result:
#     print(res)

# def Downloader(url):
#     response = requests.get(url, stream=True)
#     response_lines = response.iter_lines()
#     for lines in response_lines:
#         yield lines
#
#
# if __name__ == "__main__":
#     with open("habr.html", "wb") as file:
#         result = Downloader("http://habr.com")
#         for line in result:
#             file.write(line)
