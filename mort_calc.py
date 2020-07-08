import tkinter as tk
from tkinter import font
import numpy as np


# Function to return monthly payments
def get_mort(interest, value, years):
    print("Button clicked")

    while True:
        try:
            interest = float(interest)
            interest = interest/100
            value = float(value)
            years = float(years)

            monthly_payment = -1 * np.pmt(interest/12, years * 12, value)
            display_label['text'] = '$'+str(monthly_payment.round(2))



        except:
            display_label['text'] = 'Please type a number'
            break

        else:
            break


height = 400
width = 500

root = tk.Tk()

root.title("Monthly Mortgage Calculator")

# canvas which determines size of window
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

# Background image
background_image = tk.PhotoImage(file='land.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Frame
frame = tk.Frame(root, bg='#2E9AFE')
frame.place(relx=0.08, rely=0.07, relwidth=0.85, relheight=0.70)

# Made by Program Explorers
creator = tk.Label(
    root,
    font=('Futura', 15),
    text="Made by Program Explorers",
    foreground="#6E6E6E",  # Set the text color to white
    background="#04B431"  # Set the background color to black
)
creator.place(relx=0, rely=0.92, relwidth=0.44, relheight=0.06)

# Mortgage value
value_label = tk.Label(frame, text="Mortgage Value  $")
value_label.place(relx=0.373, rely=0.10, relwidth=0.27, relheight=0.09)

value = tk.Entry(frame, bg='#BDBDBD')
value.place(relx=0.32, rely=0.20, relwidth=0.35, relheight=0.1)

# Interest
interest_label = tk.Label(frame, text="Interest  %")
interest_label.place(relx=0.19, rely=0.38, relwidth=0.19, relheight=0.09)

interest = tk.Entry(frame, bg='#BDBDBD')
interest.place(relx=0.12, rely=0.48, relwidth=0.33, relheight=0.1)

# Num years
num_years_label = tk.Label(frame, text="Number of Years")
num_years_label.place(relx=0.595, rely=0.38, relwidth=0.255, relheight=0.09)

years = tk.Entry(frame, bg='#BDBDBD')
years.place(relx=0.54, rely=0.48, relwidth=0.35, relheight=0.1)

slider = tk.Scale(frame, from=0, to=3, orient='horizontal', resolution=0.1)
slider.place(relx=0.32, rely=0.65, relwidth=0.35, relheight=0.15)

# Get Mortgage Button
button = tk.Button(frame, text='Get Mortgage', bg='#E6E6E6',
                   command=lambda: get_mort(interest.get(), value.get(), years.get()))
button.place(relx=0.3, rely=0.82, relwidth=0.4, relheight=0.12)

lower_frame = tk.Frame(root, bg='#2E9AFE')
lower_frame.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor='n')

display_label = tk.Label(lower_frame)
display_label.place(relx=0.016, rely=0.12, relwidth=0.965, relheight=0.75)
root.mainloop()
