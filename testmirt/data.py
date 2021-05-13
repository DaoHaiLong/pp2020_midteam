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
if __name__ == '__main__':
    CreateTable()