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


def insert_customer_table(con, cus, ):
    sql = '''INSERT INTO Customer(Full_Name, Phone ,Number_people,Arrive_time)
             VALUES(?,?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, cus)
    con.commit()
    return cur.lastrowid

def insert_ordering_table(con, oder):
    sql = '''INSERT INTO Ordering(NameOrder,CustomerId )
             VALUES(?,?) '''
    cur = con.cursor()
    cur.execute(sql, oder)
    con.commit()
    return cur.lastrowid


def insert_dishes_table(con, dis):
    sql = '''INSERT INTO Dishes(Dish_name, Price)
                     VALUES(?,?) '''
    cur = con.cursor()
    cur.execute(sql, dis)
    con.commit()
    return cur.lastrowid


def insert_dishes_ordering_table(con, dishesorder):
    sql = '''INSERT INTO Dishes_Ordering(DishesId, OrderingId,Quantity)
                         VALUES(?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, dishesorder)
    con.commit()
    return cur.lastrowid

if __name__ == '__main__':
    pass