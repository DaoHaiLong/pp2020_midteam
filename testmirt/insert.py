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


def insert_customer_table(con, cus, ):
    sql = '''INSERT INTO Customer(Id,Full_Name, Phone ,Number_people,Arrive_time)
             VALUES(?,?,?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, cus)
    con.commit()

def insert_ordering_table(con, oder):
    sql = '''INSERT INTO Ordering(Id,CustomerId )
             VALUES(?,?) '''
    cur = con.cursor()
    cur.execute(sql, oder)
    con.commit()
    return cur.lastrowid

def insert_dishes_table(con,dis):
    sql = '''INSERT INTO Dishes(Id,Dish_name, Price)
                     VALUES(?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, dis)
    con.commit()
    return cur.lastrowid

def insert_dishes_ordering_table(con,dishesorder):
    sql = '''INSERT INTO Dishes_Ordering(Id,DishesId, OrderingId,Quantity, Price)
                         VALUES(?,?,?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, dishesorder)
    con.commit()
    return cur.lastrowid

def main():
    con = create_connection(database)
    with con:
        cus1 = (1,'dao hai long', '0136482175', 10, '1')
        cus2= (2,'doan van chuong', '0136482', 12, '2')
        insert_customer_table(con, cus1)
        insert_customer_table(con, cus2)
if __name__ == '__main__':
    main()