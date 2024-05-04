from tkinter import Tk, Label, Button, StringVar, OptionMenu, Frame, Entry, LabelFrame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def display_graph():
    global canvas

    # Clear previous graphs
    if canvas:
        canvas.get_tk_widget().destroy()

    # Get the number of graphs to display
    num_graphs = int(num_graphs_choice.get())

    # Get the selected graph options
    selected_options = [graph_choices[i].get() for i in range(num_graphs)]

    # Validate selected options
    if not selected_options:
        print("Error: Please select at least one graph.")
        return

    # Display the selected number of graphs
    for choice in selected_options:
        if choice == "Distribution Graph: Precipitation (histogram)":
            # Distribution Graph: Precipitation (histogram)
            plt.figure(figsize=(10, 6))
            plt.hist(df['Precipitation'], bins=10, color=hist_color_entry.get(), edgecolor='black')
            plt.title(title_entry.get() if title_entry.get() else 'Precipitation Distribution')
            plt.xlabel(x_label_entry.get() if x_label_entry.get() else 'Precipitation (in)')
            plt.ylabel(y_label_entry.get() if y_label_entry.get() else 'Frequency')
            plt.grid(True)
            plt.tight_layout()
            canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
            canvas.draw()
            canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

        elif choice == "Line Chart: Temperature over time":
            # Line Chart: Temperature over Time
            plt.figure(figsize=(10, 6))
            plt.plot(df['Time'], df['Temperature'], marker='o', linestyle='-')
            plt.title(title_entry.get() if title_entry.get() else 'Temperature Variation over Time')
            plt.xlabel(x_label_entry.get() if x_label_entry.get() else 'Time')
            plt.ylabel(y_label_entry.get() if y_label_entry.get() else 'Temperature (°F)')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
            canvas.draw()
            canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

        elif choice == "Bar Chart: Weather conditions frequency":
            # Bar Chart: Weather conditions frequency
            plt.figure(figsize=(10, 6))
            df['Weather'].value_counts().plot(kind='bar', color=bar_color_entry.get() if bar_color_entry.get() else 'lightgreen')
            plt.title(title_entry.get() if title_entry.get() else 'Weather Conditions Frequency')
            plt.xlabel(x_label_entry.get() if x_label_entry.get() else 'Weather Condition')
            plt.ylabel(y_label_entry.get() if y_label_entry.get() else 'Frequency')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            plt.tight_layout()
            canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
            canvas.draw()
            canvas.get_tk_widget().pack(side='top', fill='both', expand=1)


# Read the CSV file into a DataFrame
df = pd.read_csv("Weather_Data_visualization.csv")

# Convert 'Time' column to datetime format
df['Time'] = pd.to_datetime(df['Time'], format='%H')

# Create GUI window
window = Tk()
window.title("Weather Data Visualization")

# Add label
label = Label(window, text="Select the number of graphs and choose which to display:", background='yellow')
label.pack()

# Frame to hold dropdown menus and button
frame = Frame(window)
frame.pack(side='top', padx=5, pady=5)

# Options for number of graphs dropdown menu
num_graphs_options = ["1", "2", "3"]

# Variable to store selected number of graphs
num_graphs_choice = StringVar(window)
num_graphs_choice.set(num_graphs_options[0])

# Dropdown menu for number of graphs
num_graphs_dropdown_menu = OptionMenu(frame, num_graphs_choice, *num_graphs_options)
num_graphs_dropdown_menu.pack(side='left', padx=5, pady=5)

# List to store dropdown menus for graph selection
graph_choices = []

# Create dropdown menus for graph selection based on the number of graphs
for i in range(3):
    graph_choice = StringVar(window)
    graph_choice.set("Distribution Graph: Precipitation (histogram)")
    graph_dropdown_menu = OptionMenu(frame, graph_choice,
                                      "Distribution Graph: Precipitation (histogram)",
                                      "Line Chart: Temperature over time",
                                      "Bar Chart: Weather conditions frequency")
    graph_dropdown_menu.pack(side='left', padx=5, pady=5)
    graph_choices.append(graph_choice)

# Label frame for graph customization options
customization_frame = LabelFrame(window, text="Graph Customization")
customization_frame.pack(side='top', padx=5, pady=5, fill='x')

# Entry fields for customization options
Label(customization_frame, text="Title:").grid(row=0, column=0)
title_entry = Entry(customization_frame)
title_entry.grid(row=0, column=1)

Label(customization_frame, text="X Label:").grid(row=1, column=0)
x_label_entry = Entry(customization_frame)
x_label_entry.grid(row=1, column=1)

Label(customization_frame, text="Y Label:").grid(row=2, column=0)
y_label_entry = Entry(customization_frame)
y_label_entry.grid(row=2, column=1)

Label(customization_frame, text="Histogram Color:").grid(row=3, column=0)
hist_color_entry = Entry(customization_frame)
hist_color_entry.grid(row=3, column=1)

Label(customization_frame, text="Bar Chart Color:").grid(row=4, column=0)
bar_color_entry = Entry(customization_frame)
bar_color_entry.grid(row=4, column=1)

# Button to display selected graphs
button = Button(window, text="Display Graph", command=display_graph)
button.pack(side='top', padx=5, pady=5)

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
