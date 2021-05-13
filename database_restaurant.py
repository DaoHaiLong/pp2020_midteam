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


def create_table(con, sql_table):
    # Create a table from sql_table statement
    try:
        c = con.cursor()
        c.execute(sql_table)
    except Error as E:
        print(E)


def CreateTable():
    sql_create_customer_table = """CREATE TABLE IF NOT EXISTS Customer(
                                        Id					INT PRIMARY KEY ,
                                        Full_Name			VARCHAR(200) NOT NULL,
                                        Phone				VARCHAR(20) NOT NULL,
                                        Number_people		INT NOT NULL,
                                        Arrive_time			DATETIME DEFAULT CURRENT_TIMESTAMP
                                    ); """

    sql_create_dishes_table = """CREATE TABLE IF NOT EXISTS Dishes(
                                      Id				INT  PRIMARY KEY ,
                                      Dish_name		    VARCHAR(200) NOT NULL,
                                      Price			    FLOAT NOT NULL
                                    ); """

    sql_create_ordering_table = """CREATE TABLE IF NOT EXISTS Ordering(
                                      Id                INT PRIMARY KEY,
                                      CustomerId		INT NOT NULL,
                                      FOREIGN KEY (CustomerId) REFERENCES Customer(Id)
                                    ); """

    sql_create_dishes_ordering_table = """CREATE TABLE IF NOT EXISTS Dishes_Ordering(
                                        Id				INT  PRIMARY KEY ,
                                        DishesId		INT NOT NULL,
                                        OrderingId		INT NOT NULL,
                                        Quantity		INT NOT NULL,
                                        FOREIGN KEY (DishesId)   REFERENCES Dishes(Id),
                                        FOREIGN KEY (OrderingId)  REFERENCES Ordering(Id)
                                    ); """

    con = create_connection(database)
    if con is not None:
        create_table(con, sql_create_customer_table)
        create_table(con, sql_create_dishes_table)
        create_table(con, sql_create_ordering_table)
        create_table(con, sql_create_dishes_ordering_table)
    else:
        print("Error!!! Cannot create the database connection")


# -----------------------------------------------INSERT----------------------------------------------------------
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


def insert_dishes_table(con, dis):
    sql = '''INSERT INTO Dishes(Id,Dish_name, Price)
                     VALUES(?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, dis)
    con.commit()
    return cur.lastrowid


def insert_dishes_ordering_table(con, dishesorder):
    sql = '''INSERT INTO Dishes_Ordering(Id,DishesId, OrderingId,Quantity, Price)
                         VALUES(?,?,?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, dishesorder)
    con.commit()
    return cur.lastrowid


# ------------------------------------------------------UPDATE------------------------------------------
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


# ------------------------------------------------------------DELETE--------------------------------------------------------
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
    
con = create_connection(database)
def search_Customer():
    cur = con.cursor()
    cur.execute("SELECT * FROM Customer WHERE Id =2")

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    search_Customer()
    pass


