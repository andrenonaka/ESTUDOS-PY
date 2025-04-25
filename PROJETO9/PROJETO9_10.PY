import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title = 'Menus'
window.geometry('600x400')

menuBar = tk.Menu(window) #menu bar (is also a menu widget)
window.config(menu = menuBar) #do not pack, config var as menu

def label_text_change(text):
    global labelText
    labelText.set(text)

fileMenu = tk.Menu(menuBar, tearoff = False) #tearoff = false removes weird separator from standard menu
fileMenu.add_command(label = 'New', command = lambda: label_text_change('New'))
fileMenu.add_command(label = 'Open', command = lambda: label_text_change('Open'))
menuBar.add_cascade(label = "File", menu = fileMenu) #adds file menu to menu bar using .add_cascade method

labelText = tk.StringVar(value = 'Label1')
label1 = tk.Label(window, textvariable = labelText)
label1.pack()



window.mainloop()