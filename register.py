import tkinter as tk
import pymysql

def validate():
    a1=str(v1.get())
    a2=str(v2.get())
    a3=str(v3.get())
    a4=str(v4.get())
    
    if a1=='' or a2=='' or a3=='' or a4=='' or len(a4)!=10:
        v5.set("please fill properly")
    else:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='wallet')
        cur=conn.cursor()
        try:
          cur.execute("insert into users(name,email,password,phone) values('"+a1+"', '"+a2+"','"+a3+"', '"+a4+"')")
          conn.commit()
          v5.set("Inserted Sucessfully")
        except:
           conn.rollback()
        cur.close()
        conn.close()
        v5.set("inserted sucessfully")
        

root=tk.Tk()
root.title("Registration form")
root.geometry("400x400")
v1=tk.StringVar()
v2=tk.StringVar()
v3=tk.StringVar()
v4=tk.StringVar()

v5=tk.StringVar()
tk.Label(root,text="Name",fg="red",bg="yellow").grid(row=0,column=0)
tk.Entry(root,text="",textvariable=v1).grid(row=0,column=1)
tk.Label(root,text="Email",fg="red",bg="yellow").grid(row=1,column=0)
tk.Entry(root,text="",textvariable=v2).grid(row=1,column=1)
tk.Label(root,text="Password",fg="red",bg="yellow").grid(row=2,column=0)
tk.Entry(root,text="",show="*",textvariable=v3).grid(row=2,column=1)
tk.Label(root,text="Phone number",fg="red",bg="yellow").grid(row=3,column=0)
tk.Entry(root,text="",textvariable=v4).grid(row=3,column=1)



tk.Button(root,text="Register",command=validate).grid(row=4,column=1)
tk.Label(root,text="",fg="red",bg="yellow",textvariable=v5).grid(row=4,column=2)

