from tkinter import Tk, Label, Button, StringVar, OptionMenu, Frame, Entry, LabelFrame
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import subprocess

# Global variable to store graph canvas
canvas = None


# Function to display graph
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

    # Create a figure with subplots for all selected graphs
    if num_graphs == 1:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax = [ax]  # Convert to list for uniform handling
    else:
        fig, ax = plt.subplots(num_graphs, 1, figsize=(10, 6 * num_graphs))

    # Add space between subplots
    plt.subplots_adjust(hspace=0.5)

    # Display the selected number of graphs
    if num_graphs == 1:
        axs = ax  # If only one graph, use the single Axes object
    for idx, (choice, axs) in enumerate(zip(selected_options, ax), 1):
        if choice == "Distribution Graph: Precipitation (histogram)":
            # Distribution Graph: Precipitation (histogram)
            color = hist_color_entry.get() if hist_color_entry.get() else 'blue'  # Default color if entry is empty
            axs.hist(df['Precipitation'], bins=10, color=color, edgecolor='black')
            axs.set_xlabel(x_label_entry.get() if x_label_entry.get() else 'X Label')
            axs.set_ylabel(y_label_entry.get() if y_label_entry.get() else 'Y Label')
            axs.grid(True)


        elif choice == "Line Chart: Temperature over time":
            # Line Chart: Temperature over Time
            axs.plot(df['Time'], df['Temperature'], marker='o', linestyle='-')
            axs.set_xlabel(x_label_entry.get() if x_label_entry.get() else 'X Label')
            axs.set_ylabel(y_label_entry.get() if y_label_entry.get() else 'Y Label')
            axs.grid(True)

        elif choice == "Bar Chart: Weather conditions frequency":
            # Bar Chart: Weather conditions frequency
            color = bar_color_entry.get() if bar_color_entry.get() else 'lightgreen'  # Default color if entry is empty
            df['Weather'].value_counts().plot(kind='bar', color=color, ax=axs)
            axs.set_xlabel(x_label_entry.get() if x_label_entry.get() else 'X Label')
            axs.set_ylabel(y_label_entry.get() if y_label_entry.get() else 'Y Label')
            axs.grid(axis='y')

        # Set title with smaller font size
        axs.set_title(title_entry.get() if title_entry.get() else f'Graph {idx}', fontsize=10)

    plt.tight_layout()

    # Display the figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
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
display_button_frame = Frame(window)
display_button_frame.pack(side='top', padx=5, pady=5)

button = Button(display_button_frame, text="Display Graph", command=display_graph)
button.pack(side='left', padx=5, pady=5)


# Function to go back to main menu
def back_to_main_menu():
    window.destroy()
    subprocess.run(["python", "main_menu.py"])


# Button to go back to main menu
main_menu_button = Button(display_button_frame, text="Main Menu", command=back_to_main_menu)
main_menu_button.pack(side='left', padx=5, pady=5)

window.mainloop()
