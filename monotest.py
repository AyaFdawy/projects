from tkinter import *
import tkinter.messagebox
from PIL import *
from PIL import ImageTk,Image

def fun1():
    window = Tk()  # window->object name 
    window.geometry("1000x830+0+0")
    window.config(bg="red2")

    window.title("Mono")
    l=Label(window,text="Mono",bg="red2",fg="white",font=("nunito",44,"bold"))
    l.place(x=600,y=10)

    f1=Frame(window,height=730,width=800,bg="white")
    f1.place(x=20,y=80)

    #f2=Frame(window,height=730,width=880,bg="white")
    #f2.place(x=750,y=80)

    l1=Label(window,text="plain_text",bg="white",fg="red2",font=("nunito",18,"bold","italic"))
    l1.place(x=30,y=120) 
     
    e1 = Entry(window,width=25) 
    e1.place(x=200 , y=130) 
     
    
    def encrypt():
        plain_text=e1.get()
        alphabet ="abcdefghijklmnopqrstufwxyz"
        cipher_letter="bcdefghijklmnopqrstufwxyza"
        result=""
        indexval=[alphabet.index(char.lower()) for char in plain_text]
        result=result.join(cipher_letter[index_cipher] for index_cipher in indexval)
        listbox.insert(1,result)

    b9 = Button(window, text=" Cipher ",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=6,height=1,font=("nunito",20,"bold"), command=encrypt) 
    b9.place(x=500, y=130)

    listbox=Listbox(f1,width=130,height=15)
    listbox.place(x=5,y=450)
    
    window.mainloop() 


    #plain_text=input("enter the text: ")
    #plain_text="HELLO"
    print ("Cipher: " + encrypt())

