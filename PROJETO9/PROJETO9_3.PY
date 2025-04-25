import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Parallel Widgets')
window.geometry('400x200')

stringVar = tk.StringVar(value = 'test')

label = ttk.Label(master = window, textvariable = stringVar)
label.pack()

entry = ttk.Entry(master = window, textvariable = stringVar)
entry.pack()

entry2 = ttk.Entry(master = window, textvariable = stringVar)
entry2.pack()

button = ttk.Button(master = window, text = "Press here")
button.pack()

window.mainloop()