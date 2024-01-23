import tkinter
from tkinter import *

window=Tk()
window.title("Simple Calculator")
window.resizable(False,False)
window.config(bg="#17161b")
equation=""
def clear():
    global equation
    equation=""
    result_label.config(text=equation)
def show(value):
    global equation
    equation +=value
    result_label.config(text=equation)
def evaluate():
    global equation
    result=""
    if equation !="":
        try:
           result=eval(equation)
        except:
            result="error"
        result_label.config(text=result)
def remainder():
    global equation
    if equation !="":
        result=int(equation)% int(equation)
        result_label.config(text=result)








result_label=Label(window,text="",bg="gray",width=18,font=("arial",30))
result_label.grid(column=0,row=0,columnspan=4)
Button(window,text="C",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:clear()).grid(column=0,row=1)
Button(window,text="9",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("9")).grid(column=1,row=1)
Button(window,text="8",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("8")).grid(column=2,row=1)
Button(window,text="7",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("7")).grid(column=3,row=1)


Button(window,text="6",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("6")).grid(column=0,row=2)
Button(window,text="5",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("5")).grid(column=1,row=2)
Button(window,text="4",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("4")).grid(column=2,row=2)
Button(window,text="*",width=4,height=1,font=("arial",30,"bold"),bg="yellow",bd=1,fg="black",command=lambda:show("*")).grid(column=3,row=2)

Button(window,text="3",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("3")).grid(column=0,row=3)
Button(window,text="2",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("2")).grid(column=1,row=3)
Button(window,text="1",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("1")).grid(column=2,row=3)
Button(window,text="/",width=4,height=1,font=("arial",30,"bold"),bg="yellow",bd=1,fg="black",command=lambda:show("/")).grid(column=3,row=3)

Button(window,text="+",width=4,height=1,font=("arial",30,"bold"),bg="yellow",bd=1,fg="black",command=lambda:show("+")).grid(column=3,row=4)
Button(window,text="0",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("0")).grid(column=1,row=4)
Button(window,text="00",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show("00")).grid(column=2,row=4)
Button(window,text=".",width=4,height=1,font=("arial",30,"bold"),bg="#3697f5",bd=1,fg="#fff",command=lambda:show(".")).grid(column=0,row=4)

Button(window,text="-",width=4,height=1,font=("arial",30,"bold"),bg="yellow",bd=1,fg="black",command=lambda:show("-")).grid(column=0,row=5)

Button(window,text="%",width=4,height=1,font=("arial",30,"bold"),bg="yellow",bd=1,fg="black",command=lambda :show("%")).grid(column=1,row=5)
Button(window,text="=",width=8,height=1,font=("arial",30,"bold"),bg="yellow",bd=1,fg="black",command=evaluate).grid(column=2,row=5,columnspan=2)







window.mainloop()