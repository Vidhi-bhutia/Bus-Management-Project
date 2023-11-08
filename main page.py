import tkinter as tk
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import messagebox
import subprocess

def admin_login():
    # Replace "admin_login.py" with the actual Python script for admin login
    root.destroy()  # Close the current page
    subprocess.run(["python", "admin_login.py"])

def conductor_login():
    # Replace "conductor_login.py" with the actual Python script for conductor login
    root.destroy()  # Close the current page
    subprocess.run(["python", "conductor_login.py"])

def customer_login():
    root.destroy()  # Close the current page
    subprocess.run(["python", "user_login.py"], check=True)

def close_page():
    root.quit()
    messagebox.showinfo("Thanks", "Thanks for using Trip Trak, Happy journey!")

# Create the main window
root = tk.Tk()
root.title("Main Page")
root.geometry("400x700")

# Create a custom font for the description label
description_font = Font(family="Helvetica", size=14)

# Description Label with Background Color
description_label = tk.Label(root, text="Welcome to TRIP TRAK", font=description_font, bg="sky blue", fg="white")
description_label.pack(pady=20, fill="x")

# Load and display a company logo (Resized)
company_logo = PhotoImage(file="Triptrak.png")  # Replace with your company's logo file
company_logo = company_logo.subsample(2)  # Adjust the factor to resize the image
logo_label = tk.Label(root, image=company_logo)
logo_label.pack()

# Description Lines about "TRIP TRAK"
description_line1 = tk.Label(root, text="We make your journey easy and enjoyable.", font=description_font)
description_line1.pack()

description_line2 = tk.Label(root, text="Explore new horizons with TRIP TRAK.", font=description_font)
description_line2.pack()

# Description Label for "Select Your Role"
role_description = tk.Label(root, text="Please select your role to log in:", font=description_font)
role_description.pack()

# Create a custom font for the buttons
button_font = Font(family="Helvetica", size=12)

# Admin Login Button (Sky Blue)
admin_button = tk.Button(root, text="Admin Login", command=admin_login, font=button_font, bg="sky blue", fg="white")
admin_button.pack(pady=10)

# Conductor Login Button (Sky Blue)
conductor_button = tk.Button(root, text="Conductor Login", command=conductor_login, font=button_font, bg="sky blue", fg="white")
conductor_button.pack(pady=10)

# Customer Login Button (Sky Blue)
customer_button = tk.Button(root, text="Customer Login", command=customer_login, font=button_font, bg="sky blue", fg="white")
customer_button.pack(pady=10)

# Close Button (Bottom Center)
close_button = tk.Button(root, text="Close", command=close_page, font=button_font, bg="red", fg="white")
# close_button.pack(side="bottom", pady=20)
close_button.place(x=170, y=600)
root.mainloop()
