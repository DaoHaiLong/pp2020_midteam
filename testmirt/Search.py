import sqlite3
from sqlite3 import Error

database = r"D:\file\Projectmird\sqlite\lad.db"

def create_connection(db_file):
    # Create a connection to SQLite database
    con = None
    try:
        con = sqlite3.connect(db_file)
        print("Opened database successfully")
        return con
    except Error as E:
        print(E)

    return con
con = create_connection(database)
def search_Customer():
    cur = con.cursor()
    cur.execute("SELECT * FROM Customer WHERE Id =5")

    rows = cur.fetchall()

    for row in rows:
        print(row)

if __name__ == '__main__':
    search_Customer()