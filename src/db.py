
import sqlite3
from sqlite3 import Error

DATABASE = "database/sqlite.db"

def create_connection():
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(DATABASE)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

 
if __name__ == '__main__':
    create_connection()