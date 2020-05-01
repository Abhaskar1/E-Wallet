import tkinter as tk
import pymysql
from datetime import datetime
def show():
     output="Transactions : "
     count=0
     phone=9
     sql_query="""SELECT * FROM transactions where sender = %s OR reciever = %s ORDER BY date"""
     a1=str(v1.get())
     a2=str(v2.get())
     if a1=='':
        v2.set("Please Enter Details")
     else:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='wallet')
        cur=conn.cursor()
        try:
                 val=(a1,a1)
                 #print(val)
                 #print(a1)
                 cur.execute("SELECT * FROM users where id='"+a1 +"'")
                 for r1 in cur:
                     phone=r1[4]
                     #print("In 1st r1")
                 val=(phone,phone)
                 #print(val)
                 cur.execute(sql_query,val)
                 #print("EXECUTED")
                 for r2 in cur:
                         
                         
                         #print("In r2")
                    
                         amount=str(r2[3])
                         #print(amount)
                         #print("new")
                         #print(r2[2])
                         value=int(val[0])
                         #print(value)
                         
                         #print(type(r2[2]))
                         #print(type(value))
                         #print(type(val[0]))

                         #print(r2[2]==value)
                         if (r2[2]==value):
                             output=output+" + "+str(amount)+""
                             
                         else:
                             output=output+" - "+str(amount)+""
                             
               
                 
                     
                    
                     
                 v2.set(output)
                 #print(output)
         
                   
                 
                                
                 
        except:
                conn.rollback()
                v2.set("something error")

root=tk.Tk()
root.title("History")
root.geometry("400x400")
v1=tk.StringVar()
v2=tk.StringVar()
tk.Label(root,text="ID",fg="red",bg="yellow").grid(row=1,column=0)
tk.Entry(root,text="",textvariable=v1).grid(row=1,column=1)
tk.Button(root,text="Show History",command=show).grid(row=3,column=1)
tk.Label(root,text="",fg="red",bg="yellow",textvariable=v2).grid(row=4,column=0)


