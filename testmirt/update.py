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
def update_customer_table(con, customer):
    sql = ''' UPDATE Customer
              SET  Id	 = ? ,
                       Full_Name	 = ? ,
                       Phone   =?,
                       Number_people   =?,	
                       Arrive_time	=?
              WHERE Id = ?'''
    cur = con.cursor()
    cur.execute(sql, customer)
    con.commit()


def update_ordering_table(con, oderding):
    sql = ''' UPDATE  Ordering
              SET     Id  = ?,
                      NameOrder=?,
                      CustomerId = ?
              WHERE   Id =? '''
    cur = con.cursor()
    cur.execute(sql, oderding)
    con.commit()


def update_dishes(con, dishes):
    sql = ''' UPDATE  Dishes
              SET     Id			=?,
                      Dish_name		=?,
                      Price	      =?
              WHERE  Id=? '''
    cur = con.cursor()
    cur.execute(sql, dishes)
    con.commit()


def update_ordering_dishes(con, oedringshe):
    sql = ''' UPDATE Dishes_Ordering 
              SET     Id=?,
                      DishesId=?,
                      OrderingId=?,
                      Quantity=?
              WHERE Id =? '''
    cur = con.cursor()
    cur.execute(sql, oedringshe)
    con.commit()


if __name__ == '__main__':
    pass
