from tkinter import *
from tkinter import messagebox
def calculate():
     grade_list=[]
     credit_list=[]


     calc_grade = calc_entry.get().lower()
     eng_grade = eng_entry.get().lower()
     gener_grade = stat_entry.get().lower()
     cal_credit = calc_var.get()
     en_credit = eng_var.get()
     stat_credit = gen_var.get()

     credit_list.insert(0,cal_credit)
     credit_list.insert(1,en_credit)
     credit_list.insert(2,stat_credit)

     if calc_grade == "a":
          grade_list.insert(0,4*cal_credit)

     elif calc_grade == "b":
          grade_list.append(3*cal_credit)

     elif calc_grade == "c":
          grade_list.append(2*cal_credit)
     else:
         grade_list.append(cal_credit)
     if eng_grade == "a":
             grade_list.insert(1,4 * en_credit)
     elif eng_grade == "b":
             grade_list.append(3 * en_credit)
     elif eng_grade == "c":
             grade_list.append(2 * en_credit)
     else:

        grade_list.append(en_credit)
     if gener_grade  == "a":
            grade_list.insert(2,4 * stat_credit )
     elif gener_grade == "b":
            grade_list.append(3 * stat_credit )
     elif gener_grade  == "c":
            grade_list.append(2*stat_credit )
     else:
         grade_list.append(stat_credit )
     grade_sum=sum(grade_list)



     credit_sum =sum(credit_list)
     CGPA = grade_sum / credit_sum
     CGPA = round(CGPA, 2)


     cgpa_label.config(text=f"{CGPA}")
     message=messagebox.askyesno("successful",message="Do you want to do another Calculation?")
     if message ==True:
         eng_entry.delete(0,END)
         stat_entry.delete(0,END)
         calc_entry.delete(0,END)
         calc_credit.delete(0,END)
         gener_credit.delete(0,END)
         eng_credit.delete(0,END)
         cgpa_label.config(text="")









window=Tk()
window.title("CGPA Calculator App")
window.config(width=400,height=500,pady=50,padx=50)
frame=Frame(window)
frame.grid(column=0,row=0)
frame_label=LabelFrame(frame,text="Calculation of Grade point Average")
frame_label.grid(column=0,row=0)

subject=Label(frame_label,text="SUBJECT",bg="Gray")
subject.grid(column=0,row=0)

grade=Label(frame_label,text="GRADE")
grade.grid(column=1,row=0)

credit=Label(frame_label,text="CREDIT HOUR", padx=10)
credit.grid(column=2,row=0)

calculus=Label(frame_label,text="Calculus_I:",padx=10,pady=10)
calculus.grid(column=0,row=1)

calc_var=IntVar()
calc_credit=Entry(frame_label,width=7,textvariable=calc_var,relief=RIDGE,bd=10)
calc_credit.grid(column=2,row=1)

gen_var=IntVar()
gener_credit=Entry(frame_label,width=7,textvariable=gen_var,relief=RIDGE,bd=10)
gener_credit.grid(column=2,row=2)

eng_var=IntVar()
eng_credit=Entry(frame_label,width=7,textvariable=eng_var,relief=RIDGE,bd=10)
eng_credit.grid(column=2,row=3)

stat=Label(frame_label,text="General Statistics:",padx=10,pady=10)
stat.grid(column=0,row=2)

eng=Label(frame_label,text="English:",padx=10,pady=10,)
eng.grid(column=0,row=3)

cgpa=Label(frame_label,text="CGPA")
cgpa.grid(column=0,row=4)
cgpa_label=Label(frame_label,text="0")

cgpa_label.grid(column=1,row=4)
button=Button(frame_label,text="Calculate",padx=10,pady=10,bg="Black",fg="white",command=calculate,relief=RAISED,bd=8)
button.grid(column=1,row=5)

calc_entry=Entry(frame_label,width=7,relief=RIDGE,bd=10)
calc_entry.grid(column=1,row=1)
calc_entry.focus()
stat_entry=Entry(frame_label,width=7,relief=RIDGE,bd=10)
stat_entry.grid(column=1,row=2)
eng_entry=Entry(frame_label,width=7,relief=RIDGE,bd=10)
eng_entry.grid(column=1,row=3)









window.mainloop()