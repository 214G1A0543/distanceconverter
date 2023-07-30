from tkinter import *
import tkinter as tk

def convertionofunits():
    try:
        value = float(entry.get())

        # Conversion factors
        kilometers = value
        miles = value * 0.621371
        inches = value * 39370.1
        centimeters = value * 100000
        meters = value*1000
        yards = value*1093.613
        feet = value*3280.10 
        result_label.config(text=f"kilometers={kilometers:.2f} km\nmiles={miles:.2f} miles\ninches={inches:.2f} inches\ncentimeters={centimeters:.2f} cm\nmeters={meters:.2f} m\nyards={yards:.2f} yards\nfeets={feet:.2f} feet\n")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

# Create the main window
window = tk.Tk()
window.title("Unit Converter")

# Create the input entry
label=Label(window,text="Enter any number to be converted",font=("Bahnschrift",15)).place(x=60,y=10)
entry = tk.Entry(window, width=20)
entry.place(x=390,y=15)

# Create the convert button
convert_button = tk.Button(window, text="Convert", command=convertionofunits,font=("Bahnschrift",15))
convert_button.place(x=200,y=45)

# Create the label to display the result
result_label = tk.Label(window, text="",font=("Bahnschrift",15))
result_label.place(x=100,y=85)

# Start the GUI event loop
window.mainloop()
