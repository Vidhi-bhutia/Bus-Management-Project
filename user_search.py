import tkinter as tk
from tkinter.font import Font
import subprocess  # Import the subprocess module

# Create the main window for the next page
next_page = tk.Tk()
next_page.title("Trip Trak - Journey Planner")
next_page.geometry("400x700")
def execute_map_script(script_name):
    script_path = f"{script_name}.py"
    try:
        next_page.destroy()
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Error running {script_name}.py")

def go_to_map(script_name):
    execute_map_script(script_name)

def open_map(source, destination, script_name):
    go_to_map(script_name)
    
def open_main_page():
    next_page.destroy()  # Close the current page
    subprocess.run(["python", "user_login.py"]) 
# Create a custom font for the title label
title_font = Font(family="Helvetica", size=24, weight="bold")  # Increased font size and added bold

# Title Label with Blue Background and Thicker Border
title_label = tk.Label(next_page, text="TRIP TRAK", font=title_font, bg="sky blue", fg="white", bd=4)  # Increased border width
title_label.pack(pady=20, fill="x")

# Source and Destination Entry Fields
source_label = tk.Label(next_page, text="Source Location:")
source_label.pack()
source_entry = tk.Entry(next_page)
source_entry.pack()

destination_label = tk.Label(next_page, text="Destination:")
destination_label.pack()
destination_entry = tk.Entry(next_page)
destination_entry.pack()

# Enter Button
enter_button = tk.Button(next_page, text="Enter", command=lambda: open_map(source_entry.get(), destination_entry.get(), "map5"), bg="sky blue", fg="white")
enter_button.pack(pady=20)

# Recent Search Buttons
recent_search_label = tk.Label(next_page, text="Recent Searches:", font=title_font, fg="black")  # Reduce font size and change text color
recent_search_label.pack()

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
        command=lambda sn=script_name: go_to_map(sn),
        bg="sky blue",
        fg="black",
        justify=tk.LEFT  # Align text to the left
    )
    recent_search_button.pack(pady=5)


back_button = tk.Button(next_page, text="Back", command=open_main_page, bg="Navy", fg="white", font=("Arial", 12))
back_button.place(x=10, y=600)
next_page.mainloop()


