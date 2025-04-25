import tkinter as tk
from tkinter import ttk

def button_function():
    print('a button was pressed')

#window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x700')

#widgets
label = ttk.Label(master = window, text = "This is a test", font = 'Calibri 20')
label.pack()

text = tk.Text(master = window)
text.pack(pady = 10)

entry = ttk.Entry(master = window)
entry.pack(pady = 10)

label2 = ttk.Label(master = window, text = 'My label', font = 'Calibri 20')
label2.pack(pady = 10)

button = ttk.Button(master = window, text = 'A button', command = button_function)
button.pack(pady = 10)

button2 = ttk.Button(master = window, text = "The exercise button", command = lambda: print('Hello!'))
button2.pack()

window.mainloop() #uptades the GUI in real time and checks for events (clicks, mouse movement, closing window etc.)
