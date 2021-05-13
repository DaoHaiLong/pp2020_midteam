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
def delete_Customer(con, id):
    sql = 'DELETE FROM Customer WHERE Id=?'
    cur = con.cursor()
    cur.execute(sql, (id,))
    con.commit()


def delete_Disher(con, id):
    sql = 'DELETE FROM Dishes WHERE Id=?'
    cur = con.cursor()
    cur.execute(sql, (id,))
    con.commit()


def delete_ordering_table(con, id):
    sql = 'DELETE FROM Ordering WHERE Id=?'
    cur = con.cursor()
    cur.execute(sql, (id,))
    con.commit()


def delete_dishes_ordering(con, id):
    sql = 'DELETE FROM Dishes_Ordering WHERE Id=?'
    cur = con.cursor()
    cur.execute(sql, (id,))
    con.commit()


if __name__ == '__main__':
    pass
