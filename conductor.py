import tkinter as tk
from tkinter import PhotoImage
import subprocess

def continue_button_clicked():
    bus_number = bus_number_entry.get()
    print(f"Conductor is present on Bus Number: {bus_number}")
    conductor_page.destroy()  # Close the current page
    subprocess.run(["python", "conductor1.py"])  # Open the "conductor1.py" script

# Create the main window
conductor_page = tk.Tk()
conductor_page.geometry("400x400")
conductor_page.title("Conductor Page")

# Back button function
def back_button_clicked():
    conductor_page.destroy()  # Close the current page
    subprocess.run(["python", "conductor_login.py"])  # Open the "conductor1.py" script

# Back button
back_button = tk.Button(conductor_page, text="Back", command=back_button_clicked, bg="Navy", fg="white", font=("Arial", 12))
back_button.place(x=10, y=10)

# Sky blue background frame with "TRIP TRAK" title
title_frame = tk.Frame(conductor_page, bg="skyblue")
title_frame.pack(fill="x")
title_label = tk.Label(title_frame, text="TRIP TRAK", font=("Arial", 20, "bold"), bg="skyblue", pady=10)
title_label.pack()

# Add the bus image below the title
bus_image = PhotoImage(file="bus.png")
bus_image_label = tk.Label(conductor_page, image=bus_image, bg="white")
bus_image_label.image = bus_image  # Keep a reference to the image to prevent it from being garbage collected
bus_image_label.pack(pady=10)

# Bus number input
bus_number_label = tk.Label(conductor_page, text="Enter Bus Number:", font=("Arial", 12))
bus_number_label.pack(pady=10)
bus_number_entry = tk.Entry(conductor_page, font=("Arial", 12))
bus_number_entry.pack()

# Continue button
continue_button = tk.Button(conductor_page, text="Continue", command=continue_button_clicked, bg="sky blue", fg="white", font=("Arial", 12))
continue_button.pack(pady=20)

# Back button
back_button = tk.Button(conductor_page, text="Back", command=back_button_clicked, bg="Navy", fg="white", font=("Arial", 12))
back_button.place(x=10, y=300)

conductor_page.mainloop()
