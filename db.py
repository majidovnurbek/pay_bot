import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS userlar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userid INTEGER NOT NULL,
    fullname VARCHAR(234) NOT NULL
)''')



conn.commit()


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_users(self, userid, fullname):
        with self.connection:
            return self.cursor.execute("INSERT INTO userlar (userid,fullname) VALUES (?,?)", (userid, fullname))

    def get_all_users(self):
        with self.connection:
            return self.cursor.execute("SELECT userid, fullname FROM userlar").fetchall()

