import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import Scrollbar
import csv
from datetime import datetime


# Function to load CSV data and populate the scrollable schedule
def load_schedule():
    file_path = "academic_scheduleG.csv"  # Change this to your CSV file path
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Get today's date
            today_date = datetime.now().date()

            for row in reader:
                date = datetime.strptime(row['date'], "%Y_%m_%d").date()
                block_id = row['block_id']
                start_time = row['start_time']
                end_time = row['end_time']
                name = row['name']
                info = row['info']
                color = row['color']
                skrot_prowadzacego = row['skrot_prowadzacego']

                if date >= today_date:
                    schedule_label = ttk.Label(scrollable_frame,text=f"Date: {date}, Block ID: {block_id}, Start Time: {start_time}, End Time: {end_time}, Name: {name}, Info: {info}, Color: {color}, Skrot Prowadzacego: {skrot_prowadzacego}")
                    schedule_label.pack(anchor="w", padx=10, pady=5)

    except FileNotFoundError:
        status_label.config(text="File not found")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")


# Create the main application window
root = tk.Tk()
root.title("Scrollable Schedule Viewer")

# Create a frame for the scrollable schedule display
canvas = Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Create a label to display status messages
status_label = ttk.Label(root, text="")
status_label.pack(padx=10, pady=5)

# Create a button to load and display the schedule
load_button = ttk.Button(root, text="Load Schedule", command=load_schedule)
load_button.pack(padx=10, pady=5)


# Bind the canvas to the scrollable frame
def _on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


scrollable_frame.bind("<Configure>", _on_canvas_configure)

root.mainloop()
