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

def create_table(con, sql_table):
    # Create a table from sql_table statement
    try:
        c = con.cursor()
        c.execute(sql_table)
    except Error as E:
        print(E)

def CreateTable():
    sql_create_customer_table = """CREATE TABLE IF NOT EXISTS Customer(
                                        Id					INTEGER PRIMARY KEY ,
                                        Full_Name			VARCHAR(200) NOT NULL,
                                        Phone				VARCHAR(20) NOT NULL,
                                        Number_people		INTEGER NOT NULL,
                                        Arrive_time			DATETIME DEFAULT CURRENT_TIMESTAMP
                                    ); """

    sql_create_dishes_table = """CREATE TABLE IF NOT EXISTS Dishes(
                                      Id				INTEGER  PRIMARY KEY ,
                                      Dish_name		    VARCHAR(200) NOT NULL,
                                      Price			    FLOAT NOT NULL
                                    ); """

    sql_create_ordering_table = """CREATE TABLE IF NOT EXISTS Ordering(
                                      Id                 INTEGER PRIMARY KEY,
                                      NameOrder          VARCHAR(50) NOT NULL,
                                      CustomerId		INTEGER NOT NULL,
                                      FOREIGN KEY (CustomerId) REFERENCES Customer(Id)
                                    ); """

    sql_create_dishes_ordering_table = """CREATE TABLE IF NOT EXISTS Dishes_Ordering(
                                        Id				INTEGER  PRIMARY KEY ,
                                        DishesId		INTEGER NOT NULL,
                                        OrderingId		INTEGER NOT NULL,
                                        Quantity		INTEGER NOT NULL,
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


if __name__ == '__main__':
    CreateTable()