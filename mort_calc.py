import tkinter as tk


# Function to return monthly payments
def get_mort(interest):
    print("Button clicked")
    print(interest)


height = 400
width = 500

root = tk.Tk()

# canvas which determines size of window
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

# Background image
background_image = tk.PhotoImage(file='land.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Frame
frame = tk.Frame(root, bg='#2E9AFE')
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)

# title
label = tk.Label(root, text="Mortgage Calculator", bg='grey')
label.place(relx=0.33, rely=0, relwidth=0.35, relheight=0.05)

# Made by Program Explorers
creator = tk.Label(
    frame,
    text="Made by Program Explorers",
    foreground="#FA5858",  # Set the text color to white
    background="black"  # Set the background color to black
)
creator.place(relx=0.28, rely=0.02, relwidth=0.45, relheight=0.08)

# Mortgage value
value_label = tk.Label(frame, text="Mortgage Value")
value_label.place(relx=0.3845, rely=0.22, relwidth=0.23, relheight=0.09)

value = tk.Entry(frame, bg='#BDBDBD')
value.place(relx=0.32, rely=0.32, relwidth=0.35, relheight=0.1)

# Interest
interest_label = tk.Label(frame, text="Interest  %")
interest_label.place(relx=0.19, rely=0.50, relwidth=0.2, relheight=0.09)

interest = tk.Entry(frame, bg='#BDBDBD')
interest.place(relx=0.12, rely=0.60, relwidth=0.33, relheight=0.1)

# Num years
num_years_label = tk.Label(frame, text="Number of Years")
num_years_label.place(relx=0.595, rely=0.50, relwidth=0.25, relheight=0.09)

interest = tk.Entry(frame, bg='#BDBDBD')
interest.place(relx=0.54, rely=0.60, relwidth=0.35, relheight=0.1)

# Get Mortgage Button
button = tk.Button(frame, text='Get Mortgage', bg='#E6E6E6', command=lambda: get_mort(value.get()))
button.place(relx=0.30, rely=0.85, relwidth=0.4, relheight=0.12)

root.mainloop()
