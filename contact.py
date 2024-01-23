import json
import tkinter
from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Contact Book")
frame=Frame(window)
frame.grid(column=0,row=0,padx=10,pady=10)
frame_label=LabelFrame(frame,text="Contact_information")
frame_label.grid(column=0,row=0,padx=10,pady=10)
def save_data():
    f_name=fname_entry.get()
    l_name=lname_entry.get()
    phone=phone_entry.get()

    if len(phone)==0:
        messagebox.showinfo("Empty field left",message="Please fill the contact number")
    else:
        with open("Data.txt","a") as data_file:
            data=data_file.write(f"First Name:{f_name} | Last Name:{l_name}| Contact_number:{phone}\n")
        fname_entry.delete(0,END)
        lname_entry.delete(0, END)
        phone_entry.delete(0, END)
        save_button.config(text="Saved")
        messagebox.showinfo("Success",message="The information is successfully saved")
        save_button.config(text="Save")



fname_label=Label(frame_label,text="First Name")
fname_label.grid(column=0,row=0,padx=10,pady=10)

fname_entry=Entry(frame_label)
fname_entry.focus()
fname_entry.grid(column=0,row=1,padx=10,pady=10)

lname_label=Label(frame_label,text="Last Name")
lname_label.grid(column=1,row=0,padx=10,pady=10)
lname_entry=Entry(frame_label)
lname_entry.grid(column=1,row=1,padx=10,pady=10)

phone_label=Label(frame_label,text="Contact Number")
phone_label.grid(column=0,row=2,padx=10,pady=10)
phone_entry=Entry(frame_label)
phone_entry.grid(column=0,row=3,padx=10,pady=10)

save_button=Button(frame_label,text="Save",width=10,bg="black",fg="white",bd=1,command=save_data)
save_button.grid(column=1,row=4,padx=10,pady=10)
window.mainloop()