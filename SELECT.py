import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://net:net@localhost:5432/net_3')

connection = engine.connect()

sel_1 = connection.execute("""SELECT name_album, year FROM albums
                        WHERE year >= 2018;     
""").fetchall()

sel_2 = connection.execute("""SELECT Name_track, time FROM Tracks
                        WHERE time = (SELECT max(time) from tracks);
""").fetchall()

sel_3 = connection.execute("""SELECT Name_track, time FROM Tracks
                        WHERE time >= 210;
""").fetchall()

sel_4 = connection.execute("""SELECT title_collection FROM Collection
                        WHERE year_of_relese BETWEEN 2018 and 2020;
""").fetchall()

sel_5 = connection.execute("""SELECT name FROM Artist
                        WHERE name not LIKE '%% %%';
""").fetchall()

sel_6 = connection.execute("""SELECT Name_track FROM Tracks
                        WHERE Name_track LIKE '%%my%%' OR Name_track LIKE '%%мой%%';
""").fetchall()

print(sel_1)
print(sel_2)
print(sel_3)
print(sel_4)
print(sel_5)
print(sel_6)