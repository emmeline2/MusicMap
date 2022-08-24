import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) values (?,?)",
           ('First Song', 'Artist: A -- Content for the first Song')
           )

cur.execute("INSERT INTO posts (title, content) values (?,?)",
           ('Second Song', 'Artist: B -- Content for the second song')
           )

connection.commit()
connection.close()


