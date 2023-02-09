from audioop import add
import tkinter as tk
from tkinter import ttk, messagebox
# import mysql.connector from mysql
from tkinter import *
from neo4j import GraphDatabase
import json

class Neo4jConnection:
    
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response
conn = Neo4jConnection(uri="neo4j://10.7.3.81:7687", user="neo4j", pwd="123")
print(conn)
# ^ Neo4j Connected

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['customerid'])
    e2.insert(0,select['companyname'])
    e3.insert(0,select['contactname'])
    e4.insert(0,select['contacttitle'])
    e5.insert(0,select['address'])
    e6.insert(0,select['city'])
    e7.insert(0,select['region'])
    e8.insert(0,select['postalcode'])
    e9.insert(0,select['country'])
    e10.insert(0,select['phone'])
    e11.insert(0,select['fax'])



def Add():
    customerid = e1.get()
    companyname = e2.get()
    contactname = e4.get()
    contacttitle = e5.get()
    mobile =e3.get()
    address = e6.get()
    city = e7.get()
    region = e8.get()
    postalcode = e9.get()
    country = e10.get()
    phone = e11.get()
    fax = e12.get()

    data = {
       "customerid": customerid,
       "companyname": companyname,
       "contactname": contactname,
       "contacttitle": contacttitle,
       "address": address,
       "city": city,
       "region": region,
       "postalcode":postalcode,
       "country": country,
       "phone":phone,
       "fax":fax
    }
    j = json.dumps(data)
    print(j)
    query = 'MERGE (c:Customer{' +f'customerid:\'{customerid}\',' + f'companyname:\'{companyname}\',' + f'mobile:\'{mobile}\','+ f'contactname:\'{contactname}\',' + f'address:\'{address}\' ,' + f'city:\'{city}\',' + f'region:\'{region}\',' +  f'postalcode:\'{postalcode}\',' + f'country:\'{country}\','  + f'phone:\'{phone}\',' +  f'fax:\'{fax}\'' + '}) RETURN c'

    result = conn.query(query,db='neo4j')
    print(result)
    messagebox.showinfo("information", "Record Added successfully...")

def update():
    customerid = e1.get()
    companyname = e2.get()
    contactname = e4.get()
    contacttitle = e5.get()
    mobile =e3.get()
    address = e6.get()
    city = e7.get()
    region = e8.get()
    postalcode = e9.get()
    country = e10.get()
    phone = e11.get()
    fax = e12.get()

    data = {
       "customerid": customerid,
       "companyname": companyname,
       "contactname": contactname,
       "contacttitle": contacttitle,
       "address": address,
       "city": city,
       "region": region,
       "postalcode":postalcode,
       "country": country,
       "phone":phone,
       "fax":fax
    }
    j = json.dumps(data)
    print(j)
    query = 'MATCH (c:Customer{' +f'customerid:\'{customerid}\'' + '}) SET ' + f'c.companyname=\'{companyname}\',' + f'c.mobile=\'{mobile}\','+ f'c.contactname=\'{contactname}\',' + f'c.address=\'{address}\' ,' + f'c.city=\'{city}\',' + f'c.region=\'{region}\',' +  f'c.postalcode=\'{postalcode}\',' + f'c.country=\'{country}\','  + f'c.phone=\'{phone}\',' +  f'c.fax=\'{fax}\'' + ' RETURN c'

    result = conn.query(query,db='neo4j')
    print(result)
    messagebox.showinfo("information", "Record Updateddddd successfully...")


def delete():
    
    customerid = e1.get()
    query = 'MATCH (c:Customer{' + f'customerid:\'{customerid}\'' + '}) DELETE c'
    print(query)
    result = conn.query(query,db='neo4j')
    print(result)
    messagebox.showinfo("information", "Record Deleted successfully...")

def show():
        query = "MATCH (c:Customer{}) RETURN c"
        results = conn.query(query,db='neo4j')
        for result in results:
            r = result.items()[0][1]._properties
            print(r)
            listBox.insert("","end",values=(r["customerid"],r["companyname"],r["mobile"],r["contactname"],r["address"],r["city"],r["region"],r["postalcode"],r["country"],r["phone"],r["fax"]))

root = Tk()
root.geometry("1100x900")
root.configure(bg='#856ff8')
global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
global e9
global e10
global e11
global e12


tk.Label(root, text="Custom Registation", fg="red", font=(None, 30)).place(x=400, y=5)

tk.Label(root,bg='#856ff8', text="Customer ID").place(x=450, y=70)
Label(root,bg='#856ff8', text="Company Name").place(x=450, y=100)
Label(root,bg='#856ff8', text="Mobile").place(x=450, y=130)
Label(root,bg='#856ff8', text="Contact Name").place(x=450, y=160)
Label(root,bg='#856ff8', text="Contact Title").place(x=450, y=190)
Label(root,bg='#856ff8', text="Address").place(x=450, y=220)
Label(root,bg='#856ff8', text="City").place(x=450, y=250)
Label(root,bg='#856ff8', text="Region").place(x=450, y=280)
Label(root,bg='#856ff8', text="Postal Code").place(x=450, y=310)
Label(root,bg='#856ff8', text="Country").place(x=450, y=340)
Label(root,bg='#856ff8', text="Phone").place(x=450, y=370)
Label(root,bg='#856ff8', text="Fax").place(x=450, y=400)



e1 = Entry(root)
e1.place(x=590, y=10+60)

e2 = Entry(root)
e2.place(x=590, y=40+60)

e3 = Entry(root)
e3.place(x=590, y=70+60)

e4 = Entry(root)
e4.place(x=590, y=100+60)


e5 = Entry(root)
e5.place(x=590, y=130+60)


e6 = Entry(root)
e6.place(x=590, y=160+60)


e7 = Entry(root)
e7.place(x=590, y=190+60)


e8 = Entry(root)
e8.place(x=590, y=220+60)


e9 = Entry(root)
e9.place(x=590, y=250+60)


e10 = Entry(root)
e10.place(x=590, y=280+60)


e11 = Entry(root)
e11.place(x=590, y=310+60)


e12 = Entry(root)
e12.place(x=590, y=340+60)



Button(root, text="Add",command = Add,height=5, width= 10).place(x=440, y=440)
Button(root, text="update",command = update,height=5, width= 10).place(x=540, y=440)
Button(root, text="Delete",command = delete,height=5, width= 10).place(x=640, y=440)

cols = ('Customer ID', 'Company Name', 'Mobile','Contact Name','Address','City','Region','Postal Code','Country','Phone','Fax')
listBox = ttk.Treeview(root, columns=cols,selectmode="extended" ,show='headings' )

i = 1
s = "#"+" "+str(i)
for col in cols:
    listBox.heading(col, text=col)
    s = "#"+" "+str(i)
    listBox.column(s,anchor = CENTER, stretch=NO, width= 100)

    listBox.column("#0",width=1200)
    listBox.grid(row=0, column=0, columnspan=10)
    listBox.place(x=0, y=550)
    i+=1

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()
