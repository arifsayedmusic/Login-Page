# LOGIN FORM 
from tkinter import * 
import pyttsx3 
 
window=Tk() 
window.title("LOGIN") 
window.geometry("925x500+500+250") 
window.config(bg="#fff") 
window.resizable(False,False) 
 
def speak(voic): 
    assist=pyttsx3.init() 
    assist.say(voic) 
    assist.runAndWait() 
 
def signin(): 
    username=user.get() 
    passwor=password.get() 
    if username=="arifsayedmusic" and passwor=="1234": 
        screen=Toplevel(window) 
        screen.title("App") 
        screen.geometry("625x200+650+350") 
        screen.config(bg="#fff") 
        Label(screen,text="LOGIN SUCCESS",bg="white",fg="#57A1F8", 
              font=("calibri(Body)",30,"bold","italic"),pady=50).pack() 
        speak("LOGIN SUCCESS") 
        screen.mainloop() 
    elif username!="arifsayedmusic" and passwor!="1234":
        screen=Toplevel(window) 
        screen.title("App") 
        screen.geometry("625x200+650+350") 
        screen.config(bg="#fff") 
        Label(screen,text="INVALID USERNAME\n AND PASSWORD",bg="white", 
              fg="red", 
              font=("calibri(Body)",30,"bold","italic"),pady=50).pack() 
        speak("INVALID USERNAME AND PASSWORD") 
        screen.mainloop() 
    elif username!="arifsayedmusic": 
        screen=Toplevel(window) 
        screen.title("App") 
        screen.geometry("625x200+650+350") 
        screen.config(bg="#fff") 
        Label(screen,text="INVALID USERNAME",bg="white",fg="red", 
              font=("calibri(Body)",30,"bold","italic"),pady=50).pack() 
        speak("INVALID USERNAME") 
        screen.mainloop() 
    elif passwor!="1234": 
        screen=Toplevel(window) 
        screen.title("App") 
        screen.geometry("625x200+650+350") 
        screen.config(bg="#fff") 
        Label(screen,text="INVALID PASSWORD",bg="white",fg="red", 
              font=("calibri(Body)",30,"bold","italic"),pady=50).pack() 
        speak("INVALID PASSWORD") 
        screen.mainloop() 
 
img=PhotoImage(file="login.png") 
Label(window,image=img,bg="white").place(x=50,y=50) 
 
frame=Frame(window,width=350,height=350,bg="white") 
frame.place(x=480,y=70) 
 
heading=Label(frame,text="SIGN IN",bg="white",fg="#57A1F8", 
              font=("Microsoft YaHei UI light",25,"bold")) 
heading.place(x=100,y=5) 
 
def on_enter(e): 
    user.delete(0,"end") 
def on_leave(e): 
    name=user.get() 
    if (name==""): 
        user.insert(0,"Username") 
         
user=Entry(frame,width=25,border=0,bg="white",fg="black", 
           font=("Microsoft YaHei UI light",10)) 
user.place(x=33,y=80) 
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter) 
user.bind("<FocusOut>",on_leave) 
Frame(frame,width=300,height=2,bg="black").place(x=25,y=105) 
 
def on_enter(e): 
    password.delete(0,"end") 
    password.config(show="*") 
def on_leave(e): 
    name=password.get() 
    if (name==""): 
        password.insert(0,"Password") 
        password.config(show="") 
 
password=Entry(frame,width=25,border=0,bg="white",fg="black", 
               font=("Microsoft YaHei UI light",10)) 
password.place(x=33,y=150) 
password.insert(0,"Password") 
password.bind("<FocusIn>",on_enter) 
password.bind("<FocusOut>",on_leave) 
Frame(frame,width=300,height=2,bg="black").place(x=25,y=177) 
 
Button(frame,width=40,pady=7,text="Sign In",bg="#57A1F8",fg="white" 
       ,border=0,command=signin).place(x=35,y=205) 
 
Label(frame,text="Don't have an account ?",bg="white",fg="black", 
      font=("Microsoft YaHei UI light",10)).place(x=75,y=250) 
Button(frame,text="Sign Up",border=0,bg="white",fg="#57A1F8", 
       font=("Microsoft YaHei UI light",10)).place(x=225,y=248) 
 
window.mainloop()