import tkinter as tk
from tkinter import PhotoImage, messagebox
import subprocess
def update_seats():
    seat_count = seat_slider.get()
    if var.get() == 1:
        seat_status = "Available"
    else:
        seat_status = "Full"
    message = f"Updated Seat Details: {seat_count} seats {seat_status}"
    messagebox.showinfo("Update", message)

root = tk.Tk()
root.title("Update Seat Details")
root.geometry("400x700")
root.configure(bg="white")
root.resizable(False, False)
def back_button_clicked():
    root.destroy()  # Close the current page
    subprocess.run(["python", "conductor.py"]) 
# Sky blue background frame with "TRIP TRAK" title
title_frame = tk.Frame(root, bg="skyblue", bd=3, relief="solid")
title_frame.pack(fill="x")
title_label = tk.Label(title_frame, text="TRIP TRAK", font=("Arial", 20, "bold"), bg="skyblue", pady=10)
title_label.pack()

# Blue background frame with "UPDATE SEAT"
update_frame = tk.Frame(root, bg="blue")
update_frame.pack(fill="x")
update_label = tk.Label(update_frame, text="UPDATE SEAT", font=("Arial", 15, "bold"), bg="blue", fg="white")
update_label.pack()

# Image
img = PhotoImage(file="image.png")
image_label = tk.Label(root, image=img, bg="white")
image_label.pack()

# Slider for seat availability
seat_slider = tk.Scale(root, from_=1, to=50, orient="horizontal", length=200, label="Seats Available", font=("Arial", 12))
seat_slider.pack(pady=20)

# Radio buttons
var = tk.IntVar()
available_radio = tk.Radiobutton(root, text="Available", variable=var, value=1, font=("Arial", 12), bg="white")
available_radio.pack()
full_radio = tk.Radiobutton(root, text="Full", variable=var, value=2, font=("Arial", 12), bg="white")
full_radio.pack()

# Update Details Button
update_button = tk.Button(root, text="Update Details", command=update_seats, bg="sky blue", fg="black", font=("Arial", 12))
update_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="white")
result_label.pack()

back_button = tk.Button(root, text="Back", command=back_button_clicked, bg="Navy", fg="white", font=("Arial", 12))
back_button.place(x=10, y=600)

root.mainloop()
