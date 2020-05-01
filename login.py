import tkinter as tk
import pymysql
import welcome

def validate():
   
    a2=str(v2.get())
    a3=str(v3.get())
    if a2=='' or a3=='':
        v4.set("please filled properly")
    else:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='wallet')
        cur=conn.cursor()
        try:
          cur.execute("select * from users where email='"+a2+"' and password='"+a3+"'")
          for r1 in cur:
              root.destroy()
              welcome.omega(r1[1],r1[5],r1[0])
              
          v4.set("invalid login details")
        except:
           conn.rollback()
           v4.set("something error")
        cur.close()
        conn.close()
        

root=tk.Tk()
root.title("Login form")
root.geometry("400x400")
v2=tk.StringVar()
v3=tk.StringVar()
v4=tk.StringVar()

tk.Label(root,text="Email",fg="red",bg="yellow").grid(row=1,column=0)
tk.Entry(root,text="",textvariable=v2).grid(row=1,column=1)
tk.Label(root,text="Password",fg="red",bg="yellow").grid(row=2,column=0)
tk.Entry(root,text="",show="*",textvariable=v3).grid(row=2,column=1)

tk.Button(root,text="Login",command=validate).grid(row=3,column=1)
tk.Label(root,text="",fg="red",bg="yellow",textvariable=v4).grid(row=4,column=1)
