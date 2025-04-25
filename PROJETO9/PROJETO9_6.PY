import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Button Commands')
window.geometry('200x100')

entryVar = tk.StringVar()
entry = ttk.Entry(window, text = 'teste', textvariable = entryVar)
entry.pack()

def button_press(entry):
    print(entryVar.get())

button = tk.Button(window, text = 'Press me', command = lambda: button_press(entryVar))
button.pack()

window.mainloop()