# https://docs.python.org/3.7/library/sqlite3.html
import sqlite3
from sqlite3 import Error

DATABASE = "database/default.db"

def create_connection():
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(DATABASE)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)


def getSubscriptions():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT ID, Name FROM Subscriptions ORDER BY Name")
    result  = cur.fetchall()
    conn.close()
    return result
if __name__ == '__main__':
    print (getSubscriptions())
