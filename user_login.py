import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

def save_data_and_continue():
    name = name_entry.get()
    gender = gender_var.get()
    if name and gender:
        with open("user_details.txt", "a") as file:
            file.write(f"Name: {name}, Gender: {gender}\n")
        root.destroy()  # Close the current page
        subprocess.run(["python", "user_search.py"])
    else:
        messagebox.showerror("Error", "Please fill in all fields.")


def open_main_page():
    root.destroy()  # Close the current page
    subprocess.run(["python", "main page.py"])  # Open the "main.py" script
    
root = tk.Tk()
root.title("User Registration")
root.geometry("400x700")

# Company Name and Background
company_frame = tk.Frame(root, bg="sky blue", padx=10, pady=10)
company_frame.pack(fill="x")
company_name_label = tk.Label(company_frame, text="TRIP TRAK", font=("Arial", 24), fg="white", bg="sky blue")
company_name_label.pack()

# Company Logo (Resized)
logo_image = tk.PhotoImage(file="Triptrak.png")
logo_image = logo_image.subsample(2)  # Adjust the factor to resize the image
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(pady=10)

# User Name
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Gender Dropdown
gender_label = tk.Label(root, text="Gender:")
gender_label.pack()
genders = ["Male", "Female", "Prefer not to say"]
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=genders)
gender_dropdown.pack()

# Submit Button
submit_button = tk.Button(root, text="Continue", command=save_data_and_continue)
submit_button.pack(pady=10)

# Back Button (bottom left corner)

back_button = tk.Button(root, text="Back", command=open_main_page, bg="Navy", fg="white", font=("Arial", 12))
back_button.place(x=10, y=600)


root.mainloop()
