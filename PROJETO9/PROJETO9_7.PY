import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Events')
window.geometry('1000x800')

textBox = tk.Text(window)
textBox.pack()

button = ttk.Button(window, text = 'Button')
button.pack()

def print_event(event):
    print('An event')

def print_mousewheel(event):
    print('Mousewheel.')

def get_position(event):
    print(f'x:{event.x} y:{event.y}')

button.bind('<Alt-KeyPress-a>', print_event)
#window.bind('<Motion>', get_position)
textBox.bind('<Shift-MouseWheel>', print_mousewheel)
window.mainloop()