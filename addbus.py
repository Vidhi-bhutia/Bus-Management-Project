from tkinter import *
from tkinter import messagebox
import subprocess
adm = Tk()
adm.title("AddBus")
adm.geometry("500x500+300+200")
adm.configure(bg="white")
adm.resizable(False, False)

def open_main_page():
    adm.destroy()  # Close the current page
    subprocess.run(["python", "admin menu.py"])
    
frame = Frame(adm, width=300, height=320, bg="light blue")
frame.place(x=110, y=90)

img = PhotoImage(file="image 21.png")

# Create a frame for the Label with a border
label_frame = Frame(adm, bg="white", borderwidth=2, relief="solid")
label_frame.place(x=200, y=50)

# Create the Label and display the image inside the frame
label = Label(label_frame, image=img, bg="white")
label.pack()

def from_dest_enter(event):
    if from_dest.get() == " From ":
        from_dest.delete(0, END)

from_dest = Entry(adm, width=15, fg="black", bg="white", relief="sunken", font=("Arial", 13))
from_dest.place(x=185, y=150)
from_dest.insert(0, " From ")
from_dest.bind("<FocusIn>", from_dest_enter)

def To_dest_enter(event):
    if To_dest.get() == " To ":
        To_dest.delete(0, END)

To_dest = Entry(adm, width=15, fg="black", bg="white", relief="sunken", font=("Arial", 13))
To_dest.place(x=185, y=210)
To_dest.insert(0, " To ")
To_dest.bind("<FocusIn>", To_dest_enter)
def gender_selected():
    print("Gender:", gender_var.get())

def gender_selected():
    print("Gender:", gender_var.get())

gender_var = StringVar()
gender_var.set("None")  # Set a "dummy" value initially

gender_label = Label(adm, text="Gender", bg="white", font=("Arial", 13))
gender_label.place(x=130, y=270)

male_radio = Radiobutton(adm, text="Male", variable=gender_var, value="Male", bg="white", font=("Arial", 13), command=gender_selected)
male_radio.place(x=230, y=267)

female_radio = Radiobutton(adm, text="Female", variable=gender_var, value="Female", bg="white", font=("Arial", 13), command=gender_selected)
female_radio.place(x=300, y=267)

time_label = Label(adm, text="Time", bg="white", font=("Arial", 13))
time_label.place(x=140, y=320)
time_entry = Entry(adm, width=12, fg="black", bg="white", relief="sunken", font=("Arial", 13))
time_entry.place(x=230, y=320)

def submit():
    from_destination = from_dest.get()
    gender = gender_var.get()
    time = time_entry.get()
    print("From Destination:", from_destination)
    print("Gender:", gender)
    print("Time:", time)

submit_button = Button(adm, text="Add", command=submit, bg="blue", fg="white", relief="sunken", font=("Arial", 10), width=7, height=1)
submit_button.place(x=230, y=370)

back_button = Button(adm, text="Back", command=open_main_page, bg="Navy", fg="white", font=("Arial", 12))
back_button.place(x=10, y=450)

adm.mainloop()