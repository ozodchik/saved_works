# import psycopg2
# import sqlalchemy
#
#
# engine = sqlalchemy.create_engine('postgresql://postgres:Ozodchik2712@localhost:5432/fourth_homework')
# connection = engine.connect()
# print(engine.table_names())
#
#
# # Оператор WHERE. Найдем название и год выхода альбомов, вышедших в 2018 году;
# select_1 = connection.execute('''SELECT  name, year_issue FROM albums
# WHERE year_issue BETWEEN '2018-01-01' AND '2018-12-31';
# ''').fetchall()
# print(select_1)
#
# # Найдем название и продолжительность самого длительного трека
# select_2 = connection.execute('''SELECT duration, name FROM tracks
# WHERE duration = (
#    SELECT MAX (duration)
#    FROM tracks
# );
# ''').fetchall()
# print(select_2)
#
# # Найдем название треков, продолжительность которых не менее 3,5 минуты
# select_3 = connection.execute('''SELECT  name, duration FROM tracks
# WHERE duration >= 03.50;
# ''').fetchall()
# print(select_3)
#
# # Найдем названия сборников, вышедших в период с 2018 по 2020 год включительно
# select_4 = connection.execute('''SELECT  name FROM collection
# WHERE collect_year BETWEEN '2018-01-01' AND '2020-12-31';
# ''').fetchall()
# print(select_4)
#
# # Найдем названия исполнителей, чье имя состоит из 1 слова
# select_5 = connection.execute('''SELECT executors_name FROM executors
# WHERE executors_name NOT LIKE '%% %%';
# ''').fetchall()
# print(select_5)
#
# # Найдем название треков, которые содержат слово "мой"/"my"
# select_6 = connection.execute('''SELECT name FROM Tracks
# WHERE name  LIKE '%%my%%';
# ''').fetchall()
# print(select_6)
