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


# -----------------------------------------------INSERT----------------------------------------------------------

con = create_connection(database)
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
#----------------------------------------SEARCH---------------------------
def search_Customer():
    cur = con.cursor()
    cur.execute("SELECT * FROM Customer WHERE Id =2")

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
  #  CreateTable()
    con = create_connection(database)
    with con:
        cus1 = ('daodsw', '01364824575', 10, '1')
        cus2 = ('dao hai longg', '0136481020', 15045, '3')
        dis = ('osuki', 1000000)
        dis1 = ('mame', 2540000)

        CustomerId= insert_customer_table(con, cus1)
        CustomerId1 = insert_customer_table(con, cus2)

        oder=('daoi1',CustomerId)
        oder1=('hat',CustomerId1)

        OrderingId=insert_ordering_table(con,oder)
        OrderingId1=insert_ordering_table(con,oder1)

        DishesId = insert_dishes_table(con, dis)
        DishesId1 = insert_dishes_table(con, dis1)
        dishesorder=(DishesId,OrderingId,'good')
        dishesorder1=(DishesId1,OrderingId1,'excellent')

        insert_dishes_ordering_table(con,dishesorder)
        insert_dishes_ordering_table(con,dishesorder1)








