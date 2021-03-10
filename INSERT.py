import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://net:net@localhost:5432/net_3')

connection = engine.connect()
connection.execute("""INSERT INTO Albums(Name_album, year) 
           VALUES ('Basta 40', 2020),
           ('I', 2016),
           (19, 2003),
           ('Himera', 2001),
           ('Posolon', 2018),
           ('Experience', 1992),
           ('Olympus', 2016),
           ('Bunkka', 2002),
           ('The Fat of the Land', 1997);
""")
connection.execute("""INSERT INTO Artist(Name) 
           VALUES ('Basta'),
           ('Philip Kirkorov'),
           ('Alsou'),
           ('Аria'),
           ('Alice'),
           ('Prodigy'),
           ('Timothy'),
           ('Paul Oakenfold');
""")
connection.execute("""INSERT INTO Artist_Albums(id_artist, id_album) 
           VALUES (1, 1),
           (2, 2),
           (3, 3),
           (4, 4),
           (5, 5),
           (6, 6),
           (7, 7),
           (8, 8),
           (5, 9);
""")
connection.execute("""INSERT INTO Genre(Name_ganre) 
           VALUES ('Pop'),
           ('Hip-hop'),
           ('Electronic'),
           ('Rock'),
           ('Progressive house');
""")
connection.execute("""INSERT INTO Artist_Genre(id_artist, id_genre) 
           VALUES (1, 1),
           (1, 2),
           (2, 1),
           (3, 1),
           (4, 4),
           (5, 4),
           (6, 3),
           (7, 2),
           (8, 5),
           (8, 3);
""")
connection.execute("""INSERT INTO Collection(title_collection, year_of_relese) 
           VALUES ('I see', 2020),
            ('You are my happiness', 2016),
            ('Yesterday', 2003),
            ('Best Songs', 2011),
            ('The Best', 2020),
            ('Start the Dance', 1994),
            ('Сollection', 2018),
            ('Play Dance, Vol. 09', 2011);
""")
connection.execute("""INSERT INTO Tracks(Name_track, Time, id_album)
           VALUES ('Intro', 145, 1),
            ('I see', 415, 1),
            ('Race', 386, 2),
            ('You are my happiness', 234, 2),
            ('Yesterday', 223, 3),
            ('There', 238, 3),
            ('Calm', 279, 4),
            ('Himera', 241, 4),
            ('Posolon', 278, 5),
            ('In the rain', 343, 5),
            ('Jericho', 224, 6),
            ('Out of space', 303, 6),
            ('Home', 186, 7),
            ('The keys to Paradise', 200, 7),
            ('Southern sun', 408, 8),
            ('Time of your life', 256, 8),
            ('Smack My Bitch Up', 343, 9);
""")
connection.execute("""INSERT INTO Tracks_Collection(id_track, id_collection)
           VALUES (1, 1),
           (2, 1),
           (3, 2),
           (4, 2),
           (5, 3),
           (6, 3),
           (7, 4),
           (8, 4),
           (9, 5),
           (10, 5),
           (11, 6),
           (12, 6),
           (13, 7),
           (14, 7),
           (15, 8),
           (16, 8);
""")
