import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import os

# Function to open the "Add Bus" page
def open_add_bus_page():
    admin_window.destroy()  # Close the current window
    os.system("python addbus.py")

# Function to open the "View Bus" page
def open_view_bus_page():
    admin_window.destroy()  # Close the current window
    os.system("python viewbus.py")

# Function to go back to the admin login page
def go_back():
    admin_window.destroy()  # Close the current window
    os.system("python admin_login.py")

# Create the main admin window
admin_window = tk.Tk()
admin_window.title("Admin Menu")
admin_window.geometry("500x600")
admin_window.configure(bg="#87CEFA")

# Trip Trak Label
trip_trak_label = tk.Label(admin_window, text="Trip Trak", font=("Helvetica", 20), bg="#87CEFA")
trip_trak_label.pack(pady=20)

# Admin Logo
admin_logo_image = PhotoImage(file="admin_logo.png")
admin_logo_label = tk.Label(admin_window, image=admin_logo_image, bg="#87CEFA")
admin_logo_label.pack()

# Add Bus Button
add_bus_button = tk.Button(admin_window, text="Add Bus", command=open_add_bus_page, width=20, height=2)
add_bus_button.pack(pady=20)

# View Bus Button
view_bus_button = tk.Button(admin_window, text="View Bus", command=open_view_bus_page, width=20, height=2)
view_bus_button.pack()

# Back Button
back_button = tk.Button(admin_window, text="Back", bg = "navy", fg = "white", command=go_back, width=10, height=1)
back_button.place(x=10, y=550)

admin_window.mainloop()
