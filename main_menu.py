import pandas as pd
from tkinter import Tk, Button, Label, Toplevel, Listbox, Scrollbar, MULTIPLE
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandastable import Table
import subprocess


# Function to read CSV file into DataFrame
def read_data():
    return pd.read_csv("Weather_Data_visualization.csv")


# Function to display weather visualization page
def show_weather_visualization():
    window.destroy()
    subprocess.run(["python", "weather_project.py"])


# Function to exit the application
def exit_application():
    window.destroy()


# Function to compare data
def compare_data():
    # Read the CSV file into a DataFrame
    df = read_data()

    # Create a new window for data comparison
    comparison_window = Toplevel(window)
    comparison_window.title("Data Comparison")

    # Create a listbox to select columns for comparison
    listbox = Listbox(comparison_window, selectmode=MULTIPLE)
    scrollbar = Scrollbar(comparison_window, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")
    listbox.config(yscrollcommand=scrollbar.set)

    # Populate the listbox with column names
    for column in df.columns:
        listbox.insert("end", column)
    listbox.pack(side="left", fill="both", expand=True)

    # Create a canvas for plotting
    canvas = FigureCanvasTkAgg(plt.figure(figsize=(10, 6)), master=comparison_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side="top", fill="both", expand=1)

    # Function to plot selected data
    def plot_comparison():
        selected_columns = [listbox.get(idx) for idx in listbox.curselection()]
        if len(selected_columns) >= 2:
            plt.clf()  # Clear the previous plot
            for column in selected_columns:
                plt.plot(df.index, df[column], label=column)
            plt.title("Data Comparison")
            plt.xlabel("Index")
            plt.ylabel("Value")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()

            # Display the updated plot
            canvas.draw()

    # Button to plot selected data
    plot_button = Button(comparison_window, text="Plot Selected Data", command=plot_comparison)
    plot_button.pack(pady=5)


def show_data():
    data_window = Toplevel(window)
    data_window.title("Weather Data")

    # Read the CSV file into a DataFrame
    df = pd.read_csv("Weather_Data_visualization.csv")

    # Create a PandasTable object
    pt = Table(data_window, dataframe=df)
    pt.show()


# Create GUI window
window = Tk()
window.title("Main Menu")

# Add label
label = Label(window, text="Welcome to the Weather Data Visualization Application!", background='yellow')
label.pack()

# Button to show weather visualization page again
show_weather_button = Button(window, text="Show Weather Visualization", command=show_weather_visualization)
show_weather_button.pack(pady=5)

# Button to compare data
compare_data_button = Button(window, text="Compare Data", command=compare_data)
compare_data_button.pack(pady=5)

# Button to show all data from the CSV file
show_data_button = Button(window, text="Show All Data in csv", command=show_data)
show_data_button.pack(pady=5)

# Button to exit the application
exit_button = Button(window, text="Exit", command=exit_application)
exit_button.pack(pady=5)

window.mainloop()
