import sqlite3
from contextlib import closing

DATABASE = 'twtp.db'
def connect_db():
    return sqlite3.connect(DATABASE)


with closing(connect_db()) as db:
    with open('schema.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()

db = connect_db()
db.execute('insert into entries (course, seats) values (?, ?)', ['biol416', 0])
db.execute('insert into entries (course, seats) values (?, ?)', ['biol481', 0])
db.commit()

