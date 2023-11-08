import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
import subprocess
def open_main_page():
    root.destroy()  # Close the current page
    subprocess.run(["python", "user_search.py"]) 
# Create the main window
root = tk.Tk()
root.title("TRIP TRAK")
root.geometry("400x700")

# Create a custom font for the title label
title_font = Font(family="Helvetica", size=24, weight="bold")

# Title Label with Blue Background and Thicker Border
title_label = tk.Label(root, text="TRIP TRAK", font=title_font, bg="sky blue", fg="white", bd=4)
title_label.pack(fill="x")

# Image
image_path = "i3.jpg"
image = Image.open(image_path)
image = image.resize((400, 400))  # Adjust the size as needed
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.photo = photo
image_label.pack()

# Location and Seats Labels
location_label = tk.Label(root, text="Current Location: Green Circle", font=("Helvetica", 12))
location_label.pack()

seats_label = tk.Label(root, text="Seats Available: 2", font=("Helvetica", 12))
seats_label.pack()
back_button = tk.Button(root, text="Back", command=open_main_page, bg="Navy", fg="white", font=("Arial", 12))
back_button.place(x=10, y=600)
root.mainloop()
