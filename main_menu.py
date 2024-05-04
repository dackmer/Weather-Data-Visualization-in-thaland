from tkinter import Tk, Button, Label

def show_weather_visualization():
    window.destroy()
    import weather_project

def exit_application():
    window.destroy()

# Create GUI window
window = Tk()
window.title("Main Menu")

# Add label
label = Label(window, text="Welcome to the Weather Data Visualization Application!", background='yellow')
label.pack()

# Button to show weather visualization page again
show_weather_button = Button(window, text="Show Weather Visualization", command=show_weather_visualization)
show_weather_button.pack(pady=5)

show_history_button = Button(window, text="show history")
show_history_button.pack(pady=5)

# Button to exit the application
exit_button = Button(window, text="Exit", command=exit_application)
exit_button.pack(pady=5)

window.mainloop()
