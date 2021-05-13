import sqlite3
from sqlite3 import Error

database = r"D:\file\Projectmird\sqlite\la.db"

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

def delete_dishes_ordering(con,id):
    sql = 'DELETE FROM Dishes_Ordering WHERE Id=?'
    cur = con.cursor()
    cur.execute(sql, (id,))
    con.commit()

def main():
    con = create_connection(database)
    with con:
       # cus1 = (1,'dao hai long', '0136482175', 10, '1')
       # cus2= (2,'doan van chuong', '0136482', 12, '2')
       delete_Customer(con,1)

if __name__ == '__main__':
    main()
