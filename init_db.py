import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, lat, lon) values (?,?,?,?)",
           ('Here Comes the Sun', 'The Beatles', 53, 3)
           )

cur.execute("INSERT INTO posts (title, content, lat, lon) values (?,?,?,?)",
           ('Can\'t hold us', 'Macklemore', 47, -122)
           )

connection.commit()
connection.close()