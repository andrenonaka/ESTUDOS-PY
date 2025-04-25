import tkinter as tk
from tkinter import ttk

def button_function():
    entryText = entry.get()
    label.config(text = entryText)
    if entry.state() == ():
        entry.config(state = 'disabled')
        button.config(text = 'Entry disabled')        
    else:
        entry.config(state = 'enabled')
        button.config(text = 'Entry enabled')

window = tk.Tk()
window.title('Getting and setting Widgets')
window.geometry('800x800')

label = ttk.Label(master = window, text = 'This is a Label', font = ('Calibri 16'))
label.pack(pady = 10)

entry = ttk.Entry(master = window)
entry.pack(pady = 10)

button = ttk.Button(master = window, text = 'Button', command = button_function)
button.pack(pady = 10)

window.mainloop()

