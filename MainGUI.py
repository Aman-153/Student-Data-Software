import customtkinter as ct
from tkinter import messagebox
import csv

def rollno_clone_checker():
    #Checking for Redundancy
    with open("Data.csv", "r") as file1:
        r = csv.reader(file1)
        roll_database = []
        for i in r:
            roll_database.append(i[0])
        return roll_database


def student_adder():
    with open("Data.csv", 'a', newline='') as file:
        w = csv.writer(file)
        w.writerow([roll_entry.get(),name_entry.get().title(),branch_entry.get().upper()])
        messagebox.showinfo(title="Confirmed", message=f"{name_entry.get()} was Added!")


def details_validator():
    if not roll_entry.get() or not name_entry.get() or not branch_entry.get() :
        messagebox.showerror(title="Error", message="Please Fill All Fields!")
    else:
        if roll_entry.get().isnumeric():
            if roll_entry.get() in rollno_clone_checker():
                messagebox.showerror(title="Error", message="Roll no already exists!")
            else:
                student_adder()
        else:
            messagebox.showerror(title="Error", message="Integers only!")

def delete_text():
    roll_entry.delete(0,ct.END)
    name_entry.delete(0,ct.END)
    branch_entry.delete(0,ct.END)

# GUI
app = ct.CTk()
app.geometry("600x400")
app.title("Data Storage")



# Welcome Message
welcome_text = ct.CTkLabel(app,text="Welcome to Data Storage",text_color="#f7fff7", font=("Mona-Sans-SemiBold", 30))  # Use 'Arial' for compatibility
welcome_text.place(x=100, y=30)

# Entry Field 1
roll_text = ct.CTkLabel(app,text="Roll no", font=("Mona-Sans-SemiBold", 22))
roll_text.place(x=200, y=79)
roll_entry = ct.CTkEntry(app)
roll_entry.place(x=280, y=80)


# Entry Field 2
name_text = ct.CTkLabel(app,text="Name ", font=("Mona-Sans-SemiBold", 22))
name_text.place(x=200, y=128)
name_entry = ct.CTkEntry(app)
name_entry.place(x=280, y=128)

# Entry Field 3
branch_text = ct.CTkLabel(app,text="Course & Branch ", font=("Mona-Sans-SemiBold", 22))
branch_text.place(x=90, y=178)
branch_entry = ct.CTkEntry(app)
branch_entry.place(x=280, y=176)


#SUbmit Button
submit_button = ct.CTkButton(app,text="Submit",font=("Mona-Sans-SemiBold",18),corner_radius=20,border_color="white",fg_color="#313638", command=lambda:[details_validator(),delete_text()])
submit_button.place(x=280, y=240)

app.mainloop()