from tkinter import *
import tkinter.messagebox
from PIL import *
from PIL import ImageTk,Image

def fun1():
    window = Tk()  # window->object name 
    window.geometry("1250x820+50+0")
    window.config(bg="red2")

    window.title("Play")
    l=Label(window,text="PlayFair",bg="red2",fg="white",font=("nunito",44,"bold"))
    l.place(x=450,y=10)

    f1=Frame(window,height=600,width=800,bg="white")
    f1.place(x=230,y=80)

    l1=Label(window,text="plain_text",bg="white",fg="red2",font=("nunito",18,"bold","italic"))
    l1.place(x=330,y=180) 
     
    e1 = Entry(window,width=25) 
    e1.place(x=500 , y=190) 

    l2=Label(window,text="*static key :'monarchy'",bg="white",fg="red2",font=("nunito",14,"bold","italic"))
    l2.place(x=340,y=220) 
     
    #e2 = Entry(window,width=25) 
    #e2.place(x=200 , y=160)
    
    def matrix(key):
            matrix=[]
            for e in key.upper():
                    if e not in matrix:
                            matrix.append(e)
            alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
            
            for e in alphabet:
                    if e not in matrix:
                            matrix.append(e)	
            
            #initialize a new list. Is there any elegant way to do that?
            matrix_group=[]
            for e in range(5):
                    matrix_group.append('')

            #Break it into 5*5
            matrix_group[0]=matrix[0:5]
            matrix_group[1]=matrix[5:10]
            matrix_group[2]=matrix[10:15]
            matrix_group[3]=matrix[15:20]
            matrix_group[4]=matrix[20:25]
            return matrix_group

    def message_to_digraphs(message_original):
            message=[]
            for e in message_original.upper():
                    message.append(e)

            #Delet space
            for unused in range(int(len(message))):
                    if " " in message:
                            message.remove(" ")
            i=0
            for e in range(int(len(message)/2)):
                    if message[i]==message[i+1]:
                            message.insert(i+1,'X')
                    i=i+2

            if len(message)%2==1:
                    message.append("X")
            #Grouping
            i=0
            new=[]
            for x in range(1,int(len(message)/2+1)):
                    new.append(message[i:i+2])
                    i=i+2
            return new

    def find_position(key_matrix,letter):
            x=y=0
            for i in range(5):
                    for j in range(5):
                            if key_matrix[i][j]==letter:
                                    x=i
                                    y=j

            return x,y

    def encrypt():
        message=e1.get()
        message=message_to_digraphs(message)
        key_matrix=matrix(key)
        cipher=[]
        for e in message:
            p1,q1=find_position(key_matrix,e[0])
            p2,q2=find_position(key_matrix,e[1])
            if p1==p2:
                    if q1==4:
                        q1=-1
                    if q2==4:
                            q2=-1
                    cipher.append(key_matrix[p1][q1+1])
                    cipher.append(key_matrix[p1][q2+1])		
            elif q1==q2:
                    if p1==4:
                            p1=-1;
                    if p2==4:
                            p2=-1;
                    cipher.append(key_matrix[p1+1][q1])
                    cipher.append(key_matrix[p2+1][q2])
            else:
                    cipher.append(key_matrix[p1][q2])
                    cipher.append(key_matrix[p2][q1])
        listbox.insert(END, cipher)

    def cipher_to_digraphs(cipher):
            i=0
            new=[]
            for x in range(int(len(cipher)/2)):
                    new.append(cipher[i:i+2])
                    i=i+2
            return new

    key="monarchy"

    b9 = Button(window, text=" Cipher ",activeforeground="red2",activebackground="white",bg="red2",fg="white",bd=5,relief="ridge",width=6,height=1,font=("nunito",20,"bold"), command=encrypt) 
    b9.place(x=800, y=180)

    listbox=Listbox(f1,width=60,height=10)
    listbox.place(x=220,y=300)

  #  print (encrypt())
    
    window.mainloop() 

    
    #message=e1.get()
    #print (message_to_digraphs(message))
    #print (matrix(key)) 
    

                        
