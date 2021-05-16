from tkinter import *
from PIL import *
from PIL import ImageTk,Image
 
window = Tk()  # window->object name 
window.geometry("1250x820+130+0")
window.config(bg="white")

l1=Label(window,text="Algorithms",bg="white",fg="red2",font=("nunito",44,"bold"))
l1.place(x=430,y=50)

def c1() :
    import caesartest
    caesartest.fun1()

b1=Button(window,text="ceasar cipher",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c1)
b1.place(x=100,y=200)


def c2() :
    import monotest
    monotest.fun1()

b2=Button(window,text="monoalphabetic",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c2)
b2.place(x=750,y=200)


def c3() :
    import polytest
    polytest.fun1()

b3=Button(window,text="polyalphabetic",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c3)
b3.place(x=100,y=400)

def c4() :
    import playfair
    playfair.fun1()

b4=Button(window,text="playfair",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c4)
b4.place(x=750,y=400)

def c5() :
    import destest
    destest.fun1()


b5=Button(window,text="DES",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=16,height=2,font=("nunito",28,"bold","italic"),command=c5)
b5.place(x=430,y=600)
