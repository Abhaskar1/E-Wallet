import tkinter as tk
import pymysql
from datetime import datetime

# Assuming you have a cursor named cursor you want to execute this query on:

def money():
    sql_query="""UPDATE users SET balance = %s where id = %s"""
                
    a1=str(v1.get())
    a2=str(v2.get())
    
    #print(a2)
    bal=0
    if a1=='' or a2=='':
        v3.set("Please Enter Details")
    else:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='wallet')
        cur=conn.cursor()
        #print("connected")
        
        try:
            cur.execute("SELECT * FROM users where id='"+a1 +"'")
            for r1 in cur:
                phone=r1[4]
                #print(r1)
                bal=r1[5]
                #print(bal)
                bal2=bal+int(a2)
                
                #print(bal)
                #print(bal2)
                bal2=str(bal2)
                val=(bal2,a1)
                print(val)
                cur.execute(sql_query,val)
                now = datetime.now()
                print(now)
                formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                print(formatted_date)
                cur.execute('insert into transactions(sender,reciever,amount,date) values("0",%s,%s,%s)',(phone,a2,formatted_date))

                conn.commit()
                
            v3.set("Sucessfully Added")
    
              
            
                           
            
        except:
           conn.rollback()
           v3.set("something error")
    
root=tk.Tk()
root.title("Add Money")
root.geometry("400x400")
v1=tk.StringVar()
v2=tk.StringVar()
v3=tk.StringVar()
v4=tk.StringVar()
tk.Label(root,text="ID",fg="red",bg="yellow").grid(row=1,column=0)
tk.Entry(root,text="",textvariable=v1).grid(row=1,column=1)
tk.Label(root,text="Amount",fg="red",bg="yellow").grid(row=2,column=0)
tk.Entry(root,text="",textvariable=v2).grid(row=2,column=1)
tk.Button(root,text="Add",command=money).grid(row=3,column=1)
tk.Label(root,text="",fg="red",bg="yellow",textvariable=v3).grid(row=4,column=0)

