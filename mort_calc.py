import tkinter as tk


window = tk.Tk()
label = tk.Label(text="Mortgage Calculator")
creator = tk.Label(
    text="By Program Explorers",
    foreground="green",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()
creator.pack()

value_label = tk.Label(text="Home Value")
value_label.pack()

value = tk.Entry()
value.pack()



interest_label = tk.Label(text="Interest  %")
interest_label.pack()

interest = tk.Entry()
interest.pack()

window.mainloop()
