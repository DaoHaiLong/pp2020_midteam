from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import random
import time
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="restaurant"
)

mycursor = mydb.cursor()

root = Tk()
root.title('Restaurant Management')
root.geometry("1400x800")


def addCUS():

    a=txtFull_Name.get()
    b=txtPhone.get()
    c=txtNumber_people.get()
    d=txtArrive_time.get()

    try:
        sql = "INSERT INTO Customer (Full_Name, Phone,Number_people,Arrive_time) VALUES (%s, %s,%s,%s)"
        val = (a,b,c,d)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Insert Customer successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()


def updateCUS():

    a=txtFull_Name.get()
    b=txtPhone.get()
    c=txtNumber_people.get()
    d=txtArrive_time.get()

    try:
        sql = "UPDATE Customer SET  Phone=%s,Number_people=%s,Arrive_time=%s WHERE Full_Name=%s"
        val = (a,b,c,d)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Update Customer successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()


def deleteCUS():

    a = txtFull_Name.get()
    b = txtPhone.get()
    c = txtNumber_people.get()
    d = txtArrive_time.get()

    try:
        sql = "DELETE FROM Customer WHERE Full_Name = %s"
        val=(a,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Delete Customer successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()


def addPRODUCT():
    global Dish_name
    global Price

    a = Dish_name.get()
    b = Price.get()

    try:
        sql = "INSERT INTO Dishes (Dish_name, Price) VALUES (%s, %s)"
        val = (a, b)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Insert product successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def updatePRODUCT():
    global Dish_name
    global Price

    a = Dish_name.get()
    b = Price.get()

    try:
        sql = "UPDATE Dishes SET  Price=%s WHERE Dish_name=%s"
        val = (a,b)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Update product successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def deleteCUS():
    global Dish_name
    global Price

    a = Dish_name.get()
    b = Price.get()

    try:
        sql = "DELETE FROM Dishes WHERE Dish_name = %s"
        val=(a,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("information", "Delete product successfully")

    except EXCEPTION as e:
        print(e)
        mydb.rollback()
    mydb.close()

def SearchCUS():
    root = Tk()
    root.title('Search Customer')
    root.geometry("400x600")

    sql ="SELECT * FROM Customer"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    messagebox.showinfo("information", "Delete product successfully")

    mydb.close()


def Exit():
    exit_program = messagebox.askyesno(
        title='Restaurant Management System',
        message='Confirm if you want to exit program?')
    if exit_program > 0:
        root.destroy()
    else:
        return None

def Reset():
    txtFull_Name.delete(0,END)
    txtPhone.delete(0, END)
    txtNumber_people.delete(0, END)
    txtArrive_time.delete(0,END)


mainframe = Frame(root)
mainframe.grid()
topframe = Frame(mainframe, bd=10, width=1500, height=500, padx=2, relief=RIDGE)
topframe.pack(side=TOP)

leftframe = Frame(topframe, bd=5, width=500, height=500, padx=2, relief=RIDGE)
leftframe.pack(side=LEFT)

rightframe = Frame(topframe, bd=5, width=950, height=500, padx=2, relief=RIDGE)
rightframe.pack(side=RIGHT)

rightframe1 = Frame(rightframe, bd=5, width=950, height=350, padx=5, relief=RIDGE)
rightframe1.grid(row=0, column=0)
rightframe2 = Frame(rightframe, bd=5, width=950, height=150, padx=3, relief=RIDGE)
rightframe2.grid(row=1, column=0)

bottomFrame = Frame(mainframe, bd=10, width=1500, height=300, padx=2, relief=RIDGE)
bottomFrame.pack(side=BOTTOM)



lblFull_Name = Label(leftframe, font=('arial', 12, 'bold'), text="CustomerName", padx=1)
lblFull_Name.grid(row=0, column=0, sticky=W)
txtFull_Name = Entry(leftframe, font=('arial', 12, 'bold'), width=20)
txtFull_Name.grid(row=0, column=1, pady=3, padx=20)

lblPhone = Label(leftframe, font=('arial', 12, 'bold'), text="Phone", padx=1)
lblPhone.grid(row=1, column=0, sticky=W)
txtPhone = Entry(leftframe, font=('arial', 12, 'bold'), width=20)
txtPhone.grid(row=1, column=1, pady=3, padx=20)

lblNumber_people = Label(leftframe, font=('arial', 12, 'bold'), text="Number_people", padx=1)
lblNumber_people.grid(row=2, column=0, sticky=W)
txtNumber_people = Entry(leftframe, font=('arial', 12, 'bold'), width=20)
txtNumber_people.grid(row=2, column=1, pady=3, padx=20)

lblArrive_time = Label(leftframe, font=('arial', 12, 'bold'), text="Arrive_time", padx=1)
lblArrive_time.grid(row=3, column=0, sticky=W)
txtArrive_time = Entry(leftframe, font=('arial', 12, 'bold'), width=20)
txtArrive_time.grid(row=3, column=1, pady=3, padx=20)

btnAdd = Button(bottomFrame, bd=4, font=('arial', 13, 'bold'), width=13, height=3, text='addCUS',
                     command=addCUS)
btnAdd.grid(row=0, column=1, padx=4, pady=1)

btnUpdate = Button(bottomFrame, bd=4, font=('arial', 13, 'bold'), width=13, height=3, text='updateCUS',
                        command=updateCUS)
btnUpdate.grid(row=0, column=2, padx=4, pady=1)


btnUpdate = Button(bottomFrame, bd=4, font=('arial', 13, 'bold'), width=13, height=3, text='deleteCUS',
                        command=deleteCUS)
btnUpdate.grid(row=0, column=3, padx=4, pady=1)

btnUpdate = Button(bottomFrame, bd=4, font=('arial', 13, 'bold'), width=13, height=3, text='SearchCUS',
                        command=SearchCUS)
btnUpdate.grid(row=0, column=4, padx=4, pady=1)

btnUpdate = Button(bottomFrame, bd=4, font=('arial', 13, 'bold'), width=13, height=3, text='Reset',
                        command=Reset)
btnUpdate.grid(row=0, column=5, padx=4, pady=1)

btnUpdate = Button(bottomFrame, bd=4, font=('arial', 13, 'bold'), width=13, height=3, text='Exit',
                        command=Exit)
btnUpdate.grid(row=0, column=6, padx=4, pady=1)



if __name__ =='__main__':


    root.mainloop()