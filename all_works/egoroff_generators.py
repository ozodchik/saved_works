# import hashlib
# '''Generator List'''
#
# a = [i for i in range(100) if i % 2 == 0 and i >= 50]
# print(a)
# b = [i for i in a if (i > 55) and (i < 60)]
# print(b)
#
#
# '''Generator Выражения'''
# '''чтоб преобразовать список генератор на генератор выражение просто меняем символ списка []
# на скобки () и всё главный плюс генератора выражение в том что оно не весит памяти и работает
# быстро и мы её можем заменить на список НО тоже только 1 раз!
# МИНУСЫ: по ней можно итерироватся ТОЛЬКО 1 РАЗ! Т.Е. она  выдержит только 1 обход при любом
# способе! к ней нельзя применить способ len() К ней нельзя применить индексацию как в списках!
# т.е найти элемента по индексу мы не можем '''
#
# lists_numbers = [1, 2, 3, 4, 5]
# gener = (i+1 for i in range(lists_numbers[1]))
# print(gener)
# list_gener = list(gener)
# print(list_gener)
#
# '''ФУНКЦИИ ГЕНЕРАТОРЫ'''
# '''функция генератор с помощи yield возвращает нам 1(первое) значение и замараживает
# пока мы не вызовим её второй раз'''
#
# def gener_ex(file_name):
#     for i in file_name:
#         my_hash = hashlib.md5(i)
#         yield my_hash.hexdigest()
#
#
# with open("C:/Users/озод/PycharmProjects/first/second_pro_homework/file.txt", "rb") as file:
#     a = gener_ex(file)
#     file.readline()
#     for b in a:
#         print(b)

#
# a = [1, 2, 3, 4, 5]
# b = f'{a[4]}' * 4
# c = a[4] * 4
# print(type(f"{b}"))
# print(b)
# print(type(c))
# print(c)


#
#
# def bubble_sort(somelist):
#     last = len(somelist) - 1
#     for i in range(0, last):
#         for b in range(0, last - i):
#             if somelist[b] > somelist[b + 1]:
#                 somelist[b], somelist[b + 1] = somelist[b + 1], somelist[b]
#             print(somelist)
#
#     return somelist


# a.sort()
# print(f'other sort: {a}')

# a = "hello world"
# b = a.split()
# print(b[0])

# def is_acceptable_password(password: str) -> bool:
#     # your code her
#     a = len(password)
#     b = True
#     c = False
#     if a >= 6:
#         return b
#     else:
#         return c
#
#
# is_acceptable_password("longest")

# def hello(z):
#     if z == 0:
#         return
#     else:
#         print("hello")
#         hello(z - 1)
#
#
# hello(5)
#
# argument = [1, 2, 3, 4, 5]
