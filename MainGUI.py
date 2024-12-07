import tkinter as t
from tkinter import messagebox
import csv

def submit():
    student_roll = roll_entry.get()
    student_name = name_entry.get()
    student_course = branch_entry.get()

    #Checking for Redundancy
    with open("Data.csv", "r") as file1:
        r = csv.reader(file1)
        ap = []
        for i in r:
            ap.append(i[0])
        file1.close()


    with open("Data.csv",'a',newline='') as file:
        if not roll_entry.get() or not name_entry.get() or not branch_entry.get():
            messagebox.showerror(title="Error", message="Please Fill All Fields!")
        else:
            if roll_entry.get().isnumeric():
                if roll_entry.get() in ap:
                    messagebox.showerror(title="Error", message="Roll no already exists!")
                else:
                    w = csv.writer(file)
                    w.writerow([student_roll,student_name,student_course])
                    messagebox.showinfo(title="Confirmed", message=f"{name_entry.get()} was Added!")
            else:
                messagebox.showerror(title="Error", message="Integers only in Roll no!")


def delete_text():
    roll_entry.delete(0,t.END)
    name_entry.delete(0,t.END)
    branch_entry.delete(0,t.END)



# GUI
tk = t.Tk()
tk.geometry("600x400")
tk.title("Data Storage")


# Welcome Message
welcome_text = t.Label(text="Welcome to Data Storage", font=("Arial", 25))  # Use 'Arial' for compatibility
welcome_text.place(x=100, y=0)

# Entry Field 1
roll_text = t.Label(text="Roll no", font=("Arial", 18))
roll_text.place(x=190, y=70)
roll_entry = t.Entry()
roll_entry.place(x=280, y=80)


# Entry Field 2
name_text = t.Label(text="Name ", font=("Arial", 18))
name_text.place(x=200, y=120)
name_entry = t.Entry()
name_entry.place(x=280, y=128)

# Entry Field 3
branch_text = t.Label(text="Course & Branch ", font=("Arial", 18))
branch_text.place(x=80, y=170)
branch_entry = t.Entry()
branch_entry.place(x=280, y=176)


#SUbmit Button
submit_button = t.Button(text="Submit", command=lambda:[submit(),delete_text()])
submit_button.place(x=280, y=240)


tk.mainloop()