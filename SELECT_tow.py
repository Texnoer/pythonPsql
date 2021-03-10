import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://net:net@localhost:5432/net_3')

connection = engine.connect()
# количество исполнителей в каждом жанре
sel_1 = connection.execute("""SELECT g.Name_ganre, COUNT(a.id_artist)  FROM Genre g
            LEFT JOIN Artist_Genre a ON g.id_genre = a.id_genre
            GROUP BY Name_ganre;
""").fetchall()
# количество треков, вошедших в альбомы 2019-2020 годов
sel_2 = connection.execute("""SELECT a.year, COUNT(Name_track) FROM Tracks t
            LEFT JOIN albums a ON a.id_album = t.id_album
            WHERE year >= 2019
            GROUP BY year;
""").fetchall()
# средняя продолжительность треков по каждому альбому
sel_3 = connection.execute("""SELECT Name_album, AVG(Time) FROM Tracks t
            LEFT JOIN albums a ON a.id_album = t.id_album
            GROUP BY Name_album;
""").fetchall()
# все исполнители, которые не выпустили альбомы в 2020 году
sel_4 = connection.execute("""SELECT Name FROM Artist ar
            LEFT JOIN Artist_Albums a_a ON a_a.id_artist = ar.id_artist
            LEFT JOIN albums al ON al.id_album = a_a.id_album
            WHERE year < 2020
            GROUP BY Name;
""").fetchall()
# названия сборников, в которых присутствует конкретный исполнитель (выберите сами)
sel_5 = connection.execute("""SELECT title_collection FROM Collection c
            LEFT JOIN Tracks_Collection tc ON tc.id_collection = c.id_collection
            LEFT JOIN Tracks t ON t.id_track = tc.id_track
            LEFT JOIN albums al ON al.id_album = t.id_album
            LEFT JOIN Artist_Albums aa ON aa.id_album = al.id_album
            LEFT JOIN artist a ON a.id_artist = aa.id_artist
            WHERE name = 'Alsou'
            GROUP BY title_collection;
""").fetchall()
# название альбомов, в которых присутствуют исполнители более 1 жанра;
sel_6 = connection.execute("""SELECT al.Name_album, COUNT(ag.id_artist) FROM Albums al
            LEFT JOIN Artist_Albums aa ON aa.id_album = al.id_album
            LEFT JOIN artist a ON a.id_artist = aa.id_artist
            LEFT JOIN Artist_Genre ag ON ag.id_artist = a.id_artist
            GROUP BY Name_album
            HAVING COUNT(ag.id_artist) > 1;
""").fetchall()
# наименование треков, которые не входят в сборники;
sel_7 = connection.execute("""SELECT Name_track FROM Tracks t
            LEFT JOIN Tracks_Collection tc ON tc.id_track = t.id_track
            LEFT JOIN Collection c ON c.id_collection = tc.id_collection
            WHERE tc.id_collection IS NULL
            GROUP BY Name_track;
""").fetchall()
# исполнителя(-ей), написавшего самый короткий по продолжительности трек
# (теоретически таких треков может быть несколько)
sel_8 = connection.execute("""SELECT a.Name FROM Artist a
            LEFT JOIN Artist_Albums aa ON aa.id_artist = a.id_artist
            LEFT JOIN albums al ON al.id_album = aa.id_album
            LEFT JOIN tracks t ON t.id_album = al.id_album
            GROUP BY a.Name, t.time
            HAVING time = (select MIN(time) FROM tracks)
;
""").fetchall()
# название альбомов, содержащих наименьшее количество треков
sel_9 = connection.execute("""SELECT Name_album FROM albums a
            LEFT JOIN tracks t ON t.id_album = a.id_album
            GROUP BY Name_album
            HAVING count(name_track) < count(*);
""").fetchall()

print(1, sel_1)
print(2, sel_2)
print(3, sel_3)
print(4, sel_4)
print(5, sel_5)
print(6, sel_6)
print(7, sel_7)
print(8, sel_8)
print(9, sel_9)