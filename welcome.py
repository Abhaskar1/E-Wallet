import tkinter as tk
import pymysql

def logout(root):
   root.destroy()
   import login
def add(root):
   root.destroy()
   import add
def pay(root):
   root.destroy()
   import pay
   
def recharge(root):
   root.destroy()
   import recharge
   
def ticket(root):
   root.destroy()
   import ticket
  
def bill(root):
   root.destroy()
   import bill
   
def history(root):
   root.destroy()
   import history
def logout(root):
   root.destroy()
   import login
   
   
def omega(p,q,i):
    root=tk.Tk()
    root.title("Welcome Page")
    root.geometry("400x400")
    v2=tk.StringVar()
    v3=tk.StringVar()
    v4=tk.StringVar()
    v5=tk.StringVar()
    v6=tk.StringVar()
    v6.set(i)
    v2.set(str(p))
    v5.set(str(q))
    tk.Label(root,text="Welcome",fg="red",bg="yellow").grid(row=0,column=0)
    tk.Label(root,text="name",fg="red",bg="yellow",textvariable=v2).grid(row=0,column=1)
    tk.Label(root,text="Your ID",fg="red",bg="yellow").grid(row=1,column=0)
    tk.Label(root,text=i,fg="red",bg="yellow").grid(row=1,column=1)
    tk.Label(root,text="Balance:",fg="red",bg="yellow").grid(row=2,column=0)
    tk.Label(root,text=q,fg="red",bg="yellow").grid(row=2,column=1)
  
   

    tk.Button(root,text="Add Money",command=lambda:add(root)).grid(row=4,column=2)
    tk.Button(root,text="Pay",command=lambda:pay(root)).grid(row=5,column=2)
    tk.Button(root,text="Recharge",command=lambda:recharge(root)).grid(row=6,column=2)
    tk.Button(root,text="Movie Ticket",command=lambda:ticket(root)).grid(row=7,column=2)
    tk.Button(root,text="Electric Bill",command=lambda:bill(root)).grid(row=8,column=2)
    tk.Button(root,text="History",command=lambda:history(root)).grid(row=9,column=2)
    tk.Button(root,text="Logout",command=lambda:logout(root)).grid(row=10,column=2)
