import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, StringVar, OptionMenu, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def display_graph():
    global canvas

    # Clear previous graph
    if canvas:
        canvas.get_tk_widget().destroy()

    choice = graph_choice.get()

    if choice == "Distribution Graph: Precipitation (histogram)":
        # Distribution Graph: Precipitation (histogram)
        plt.figure(figsize=(10, 6))
        plt.hist(df['Precipitation'], bins=10, color='skyblue', edgecolor='black')
        plt.title('Precipitation Distribution')
        plt.xlabel('Precipitation (in)')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    elif choice == "Line Chart: Temperature over time":
        # Line Chart: Temperature over Time
        plt.figure(figsize=(10, 6))
        plt.plot(df['Time'], df['Temperature'], marker='o', linestyle='-')
        plt.title('Temperature Variation over Time')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°F)')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    elif choice == "Bar Chart: Weather conditions frequency":
        # Bar Chart: Weather conditions frequency
        plt.figure(figsize=(10, 6))
        df['Weather'].value_counts().plot(kind='bar', color='lightgreen')
        plt.title('Weather Conditions Frequency')
        plt.xlabel('Weather Condition')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    else:
        print("Invalid choice. Please select a graph.")


# Read the CSV file into a DataFrame
df = pd.read_csv("Weather_Data_visualization.csv")

# Convert 'Time' column to datetime format
df['Time'] = pd.to_datetime(df['Time'], format='%H')

# Create GUI window
window = Tk()
window.title("Weather Data Visualization")

# Add label
label = Label(window, text="Select a graph to display:", background='yellow')
label.pack()

# Frame to hold dropdown menu and button
frame = Frame(window)
frame.pack(side='top', padx=5, pady=5)

# Options for dropdown menu
graph_options = [
    "Distribution Graph: Precipitation (histogram)",
    "Line Chart: Temperature over time",
    "Bar Chart: Weather conditions frequency"
]

# Variable to store selected option
graph_choice = StringVar(window)
graph_choice.set(graph_options[0])

# Dropdown menu
dropdown_menu = OptionMenu(frame, graph_choice, *graph_options)
dropdown_menu.pack(side='left', padx=5, pady=5)

# Button to display selected graph
button = Button(frame, text="Display Graph", command=display_graph)
button.pack(side='left', padx=5, pady=5)

# Global variable to store graph canvas
canvas = None

# Function to display graph canvas
def display_graph_canvas():
    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

# Call the function to display graph canvas
display_graph_canvas()

window.mainloop()