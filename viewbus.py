import tkinter as tk
from tkinter.font import Font
import subprocess  # Import the subprocess module

# Create the main window for the next page
next_page = tk.Tk()
next_page.title("Trip Trak - Journey Planner")
next_page.geometry("400x400")

def back_button_clicked():
    next_page.destroy()  # Close the current page
    subprocess.run(["python", "admin menu.py"])

# Create a custom font for the title label
title_font = Font(family="Helvetica", size=24, weight="bold")  # Increased font size and added bold

# Title Label with Blue Background and Thicker Border
title_label = tk.Label(next_page, text="TRIP TRAK", font=title_font, bg="sky blue", fg="white", bd=4)  # Increased border width
title_label.pack(pady=20, fill="x")


# Sample Recent Search Data
recent_search_data = [
    ("Bus no. 1A (Ladies Special)", "Circuit House to VIT University"),
    ("Bus no. 2B", "Raja Theatre to Sevur"),
    ("Bus no. 1C (Ladies Special)", "Joyalukas to BHEL-Ranipet"),
    ("Bus no. 2A", "PVR-Velocity Mall to Serkadu")
]

script_names = ["map1", "map2", "map3", "map4"]

# Create Recent Search Buttons:
for script_name, (bus_number, route) in zip(script_names, recent_search_data):
    button_text = f"{bus_number}\n{route}"  # Combine bus number and route with a line break
    recent_search_button = tk.Button(
        next_page,
        text=button_text,
        bg="sky blue",
        fg="black",
        justify=tk.CENTER  # Align text to the left
    )
    recent_search_button.pack(pady=10)

back_button = tk.Button(next_page, text="Back", command=back_button_clicked, bg="Navy", fg="white", font=("Arial", 12))
back_button.place(x=10, y=350)

next_page.mainloop()
