import tkinter as tk
import pymysql
from datetime import datetime
def money():
    sql_query="""UPDATE users SET balance = %s where id = %s"""
    sql_q2="""SELECT phone FROM users WHERE phone = %s"""
    sql_q3="""UPDATE users SET balance = %s where phone = %s"""
    sql_q4="""SELECT * FROM users where phone = %s"""
                
    a1=str(v1.get())
    a2=str(v2.get())
    a3=str(v4.get())
    #print(a3)
    found=0
   
    flag=1
    
    #print(a2)
    bal=0
    if a1=='' or a2=='' or a3=='' or len(a3)!=10:
        v3.set("Please Enter Correct/Complete Details")
    else:
        conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='',db='wallet')
        cur=conn.cursor()
        #print("connected")
        
        try:
            val=(a3)
            #print(val)
            val=cur.execute(sql_q2,val)
            print(val)
            #print("DONE")
            if(val>0):
                found=1
                val=(a3)
                print(a3)
                balNew=cur.execute(sql_q4,a3)
                #print(balNew)
                records=cur.fetchall()
                #print(records)
                for row in records:
                    balNew=row[5]
                    #print(balNew)
                balNew=balNew+int(a2)
                
                val=(balNew,a3)
                #print(val)
                cur.execute(sql_q3,val)
                #print("Inside if")
            if(found==0):
                v3.set("Number not registered")
            else:
                cur.execute("SELECT * FROM users where id='"+a1 +"'")
                for r1 in cur:
                    #print(r1)
                    bal=r1[5]
                    #print(bal)
                    bal2=bal-int(a2)
                    if(bal2<0):
                        v3.set("Not Enough Balance")
                        flag=0
                    
                    #print(bal)
                    #print(bal2)
                    if(flag==1 and found==1):
                        phone=r1[4]
                        bal2=str(bal2)
                        val=(bal2,a1)
                        #print(val)
                        cur.execute(sql_query,val)
                        now = datetime.now()
                        print(now)
                        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                        print(formatted_date)
                        cur.execute('insert into transactions(sender,reciever,amount,date) values(%s,%s,%s,%s)',(phone,a3,a2,formatted_date))
                        conn.commit()
                        
                        v3.set("Paid")
        
              
            
                           
            
        except:
           conn.rollback()
           v3.set("something error")
    
root=tk.Tk()
root.title("Recharge")
root.geometry("400x400")
v1=tk.StringVar()
v2=tk.StringVar()
v3=tk.StringVar()
v4=tk.StringVar()
tk.Label(root,text="ID",fg="red",bg="yellow").grid(row=1,column=0)
tk.Entry(root,text="",textvariable=v1).grid(row=1,column=1)
tk.Label(root,text="Amount",fg="red",bg="yellow").grid(row=2,column=0)
tk.Entry(root,text="",textvariable=v2).grid(row=2,column=1)
tk.Label(root,text="Pay To",fg="red",bg="yellow").grid(row=3,column=0)
tk.Entry(root,text="",textvariable=v4).grid(row=3,column=1)
tk.Button(root,text="Pay",command=money).grid(row=4,column=1)
tk.Label(root,text="",fg="red",bg="yellow",textvariable=v3).grid(row=5,column=0)

