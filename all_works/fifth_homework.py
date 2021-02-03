import psycopg2
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:Ozodchik2712@localhost:5432/fifty_homework')
connection = engine.connect()
print(engine.table_names())

# insert_musicians = connection.execute('''INSERT INTO executors(executors_name)
#     VALUES ('musician_1'), ('musician_2'), ('musician_3'), ('musician_4'),
#     ('musician_5'), ('musician_6'), ('musician_7'), ('musician_8');
# ''')
# print(insert_musicians)
#
#
# insert_genres = connection.execute('''INSERT INTO genres(Name_of_genre)
#     VALUES ('genre_1'), ('genre_2'), ('genre_3'), ('genre_4'), ('genre_5');
# ''')
# print(insert_genres)
#
#
# insert_albums = connection.execute(f'''INSERT INTO albums(name, description, year_issue)
#     VALUES ('Name_of_album_1', 'description_1', '2010-01-02 14:32:12'),
#     ('Name_of_album_2',  'description_2', '2011-11-12 16:32:12'),
#     ('Name_of_album_3',  'description_3', '2007-01-02 12:34:12'),
#     ('Name_of_album_4',  'description_4', '2019-11-12 14:32:12'),
#     ('Name_of_album_5',  'description_5', '2016-07-07 19:32:12'),
#     ('Name_of_album_6',  'description_6', '2018-01-02 14:32:12'),
#     ('Name_of_album_7',  'description_7', '2010-09-02 14:32:12'),
#     ('Name_of_album_8',  'description_8', '2020-01-02 14:32:12');
# ''')
# print(insert_albums)
#
#
# insert_tracks = connection.execute('''INSERT INTO tracks(Name, Duration, albums_id)
#     VALUES ('Track_1', 02.02, 73),
#     ('Track_2', 03.02, 74), ('Track_3', 01.23, 75), ('Track_4', 01.13, 76),
#     ('Track_5', 02.02, 77), ('Track_6', 01.43, 78), ('Track_7', 01.15, 79),
#     ('Track_8', 01.02, 80), ('Track_9', 01.54, 73), ('Track_10', 01.46, 74),
#     ('Track_11', 03.02, 75), ('Track_12', 01.34, 76), ('Track_13', 01.33, 77),
#     ('Track_14', 01.02, 78), ('Track_15', 01.23, 79), ('Track_16', 01.27, 80);
# ''')

#
# insert_collections = connection.execute('''INSERT INTO
#     collection(name, collect_year)
#     VALUES ('Name_of_collection_1', '2011-05-16 15:36:38'),
#     ('Name_of_collection_2', '2019-03-23 15:36:38'),
#     ('Name_of_collection_3', '2020-01-24 15:36:38'),
#     ('Name_of_collection_4', '2019-05-25 15:36:38'),
#     ('Name_of_collection_5', '2020-11-26 15:36:38'),
#     ('Name_of_collection_6', '2019-01-28 15:36:38'),
#     ('Name_of_collection_7', '2020-05-21 15:36:38'),
#     ('Name_of_collection_8', '2019-11-21 15:36:38');
# ''')
# print(insert_collections)


# Insert. заполним таблицу связей Executors_Genres
# insert_executors_genres = connection.execute('''INSERT INTO
#     Executors_Genres(id_of_executor, id_of_genre)
#     VALUES (73, 46),
#     (74, 47),
#     (75, 48),
#     (76, 49),
#     (77, 50),
#     (78, 46),
#     (79, 47),
#     (80, 48);
# ''')
# print(insert_executors_genres)


# insert_executors_albums = connection.execute('''INSERT INTO
#     executors_albums(executors_id, albums_id)
#     VALUES (73, 73),
#     (74, 74),
#     (75, 75),
#     (76, 76),
#     (77, 77),
#     (78, 78),
#     (79, 79),
#     (80, 80);
# ''')
# print(insert_executors_albums)
#
#
#
# insert_executors_albums = connection.execute('''INSERT INTO
#     trscks_collection(tracks_id, collection_id)
#     VALUES (113, 49), (114, 50), (115, 51), (116, 52), (117, 53), (118, 54), (119, 55), (120, 56),
#     (121, 49), (122, 50), (123, 51), (124, 52), (125, 53), (126, 54), (127, 55), (128, 56);
# ''')
# print(insert_executors_albums)
# #
#
#
# # Insert. Добавим сверху еще 2 альбома для задания №2 (SELECT)
# insert_albums_additionally = connection.execute(f'''INSERT INTO Albums(name, description, year_issue)
#     VALUES ('Name_of_album_1', 'my_regular_loren_ipsum_1', '2011-05-16 15:36:38'),
#     ('Name_of_album_xx', 'my_regular_loren_ipsum_xx', '2018-03-09 15:36:38'),
#     ('Name_of_album_yy', 'my_regular_loren_ipsum_yy', '2018-01-16 15:36:38');
# ''')
# print(insert_albums_additionally)
#
#
# # Insert. Добавим сверху еще 2 трека для задания №2 (SELECT)
# insert_tracks_additionally = connection.execute('''INSERT INTO Tracks(Name, Duration, albums_id)
#     VALUES ('Track_n', 05.01, 74), ('Track_m', 04.22, 74);
# ''')
# print(insert_tracks_additionally)
#
#
# # Insert. Добавим сверху еще 2 трека с 'my' для задания №2 (SELECT)
# insert_tracks_additionally_my = connection.execute('''INSERT INTO Tracks(Name, Duration, albums_id)
#     VALUES ('mymymymymymymymymy', 06.01, 75), ('Track_my', 04.52, 76);
# ''')
# print(insert_tracks_additionally_my)









# sel_1 = connection.execute("""
# select id_of_genre, count(id_of_executor) from executors_genres
# group by id_of_genre
# order by id_of_genre;
# """).fetchall()
# print(sel_1)


# Найдем количество треков, вошедших в альбомы 2019-2020 годов
# sel_2 = connection.execute("""
# select count(t.id), a.name from tracks t
# join albums a on t.albums_id = a.id
# group by a.id
# having year_issue between '2019-01-01' and '2020-12-31';
# """).fetchall()
# print(sel_2)


# sel_3 = connection.execute("""
# select a.name, avg(t.duration) from albums a
# join tracks t on a.id = t.albums_id
# group by a.name
# order by a.name
# """).fetchall()
# print(sel_3)


# # Найдем всех исполнителей, которые не выпустили альбомы в 2020 году
# sel_4 = connection.execute("""
# select executors_name from executors e
# join executors_albums e_a on e.id = e_a.executors_id
# join albums a on e_a.albums_id = a.id
# group by e.executors_name, a.year_issue
# having a.year_issue not between '2020-01-01' and '2020-12-31';
# """).fetchall()
# print(sel_4)


# # Найдем названия сборников, в которых присутствует исполнитель 'musician_3'
# sel_5 = connection.execute("""
# select col.name, e.executors_name from executors e
# join executors_albums e_a on e.id = e_a.executors_id
# join albums a on e_a.albums_id = a.id
# join tracks t on a.id = t.albums_id
# join trscks_collection t_c on t.id = t_c.tracks_id
# join collection col on t_c.collection_id = col.id
# group by col.name, e.executors_name
# having e.executors_name like '%%musician_3%%';
# """).fetchall()
# print(sel_5)


# # Найдем название альбомов, в которых присутствуют исполнители более 1 жанра
# sel_6 = connection.execute("""
# select a.name, e.executors_name, g.name_of_genre from albums a
# left join executors_albums e_a on a.id = e_a.albums_id
# left join executors e on e.id = e_a.executors_id
# left join executors_genres e_g on e_g.id_of_executor = e.id
# left join genres as g on g.id = e_g.id_of_genre
# group by a.name, e.executors_name, g.name_of_genre
# having count(g.id) > 1;
# """).fetchall()
# print(sel_6)


# # Найдем названия альбомов, содержащих наименьшее количество треков
# sel_7 = connection.execute("""
# select distinct a.name from albums a
# join tracks t on t.albums_id = a.id
# where t.albums_id  in (
#     select albums_id from tracks
#     group by albums_id
#     having count(tracks.id) = (
#         select count(tracks.id) from tracks
#         group by albums_id
#         limit 1
#     )
# );
# """).fetchall()
# print(sel_7)


# # Найдем исполнителя(-ей), написавшего самый короткий по продолжительности трек
# sel_8 = connection.execute("""
# select e.executors_name, min(t.duration) from tracks as t
# left join albums a on a.id = t.albums_id
# left join executors_albums e_a on e_a.albums_id = a.id
# left join executors e on e.id = e_a.executors_id
# group by e.executors_name, t.duration
# having t.duration = (
#     select min(duration) from tracks
#     );
# """).fetchall()
# print(sel_8)


# # Найдем наименование треков, которые не входят в сборники
# sel_9 = connection.execute("""
# select t.name from tracks t
# left join trscks_collection t_c on t_c.tracks_id = t.id
# where t_c.tracks_id is null;
# """).fetchall()
# print(sel_9)