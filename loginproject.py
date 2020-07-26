from tkinter import *
import mysql.connector
import sys

def login(): 
      
    
     try:
       conn = mysql.connector.connect(host="localhost", user="admin",password="admin",database="forpython")
     except:
       print("You are not connected to server(localhost)")
     else:
       print("Connection established sucessfully")
       print("Enter your username and password ")

     
       userid = User.get()
       passw = Pass.get()

       cur = conn.cursor()
       
       #cur.execute("select * from userlogin where username=%s and password =%s",(User.get(),Pass.get()))
       cur.execute("select * from userlogin where username =%s AND password=%s",(userid,passw))
       myresult=cur.fetchall()
       print(myresult)

      

       if myresult:
           print("\nYou have logged in successfully")
           newWindow()
           
       else:
           print("\nIncorrect username/password")
       cur.close()
       conn.close()


def newWindow():
    global home
    obj.withdraw()
    home = Tk()
    home.geometry('400x350')
    home.title('Login')
    Label(home,text ='You have successfully logged in!!!:)' , font = 'Times 15').place(x=50,y=50)

    Button(home,text="Logout",font = 'Times 13',command=closew).place(x = 150, y = 135, width = 60) 
    
    home.mainloop()
  
def closew():
    home.withdraw()

    sys.exit()


def register():
   global reg,name,us,ps,gd
   obj.withdraw()
   reg = Tk()
   reg.geometry('350x300')
   reg.title('SIGNUP')
   
   Label(reg,text = 'Name : ',font = 'Times 15').place(x = 50, y = 60)
   name = Entry(reg)
   name.place(x = 150, y = 60, width = 150) 

   Label(reg,text = 'Username : ',font = 'Times 15').place(x = 50, y = 90, width = 100) 
   us = Entry(reg)
   us.place(x = 150, y = 90, width = 150)

   Label(reg,text = 'Password : ',font = 'Times 15').place(x = 50, y = 120, width = 100) 
   ps = Entry(reg)
   ps.place(x = 150, y = 120, width = 150)

   Label(reg,text = 'Gender : ',font = 'Times 15').place(x = 50, y = 150, width = 100) 
   gd = Entry(reg)
   gd.place(x = 150, y = 150, width = 150)

   Button(reg,text="Register",font = 'Times 13',command=adddetails).place(x = 150, y = 190, width = 60)
    
   reg.mainloop() 

def adddetails():
    global back
    reg.withdraw()
    back=Tk()
    
    nm=name.get()
    user=us.get()
    pwd=ps.get()
    gnd=gd.get()

    try:
       conn = mysql.connector.connect(host="localhost", user="root",password="Suteja2327!",database="forpython")
    except:
       print("You are not connected to server(localhost)")
    else:
       print("Connection established sucessfully")
      
       cur = conn.cursor()
       
       
       cur.execute("insert into userlogin values(%s,%s,%s,%s)",(nm,user,pwd,gnd))
       conn.commit()
       
       print("Records inserted into the table")
       back.geometry('400x350')
       back.title('Registration')
       Label(back,text ='You have successfully signed up!!!:)' , font = 'Times 15').place(x=50,y=50)

       Button(back,text="Close",font = 'Times 13',command=closet).place(x = 150, y = 135, width = 120)
       
       cur.close()
       conn.close()

        
def closet():
  back.withdraw()     
  sys.exit() 

     

def mainpg():
 
 global obj
 obj=Tk()
 obj.geometry('350x300')

 obj.title('LOGIN PAGE')

 global User
 global Pass

 Label(text = 'Username : ',font = 'Times 15').place(x = 50, y = 60)
 User = Entry()
 User.place(x = 150, y = 60, width = 150) 

 Label(text = 'Password : ',font = 'Times 15').place(x = 50, y = 90, width = 100) 
 Pass = Entry(show='*')
 Pass.place(x = 150, y = 90, width = 150) 

 Button(text="Login",font = 'Times 13',command=login).place(x = 150, y = 135, width = 60) 

 Label(text="Dont have an account?", font = 'Times 15').place( x=80 , y=190)

 Button(text="Signup",font = 'Times 13',command=register).place(x = 145, y = 220, width = 70)
  
 obj.mainloop()

mainpg()
