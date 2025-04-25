import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

buttonStr = tk.StringVar(value = 'A button with Str Var')
button = ttk.Button(master = window, text = 'Simple Button', command = lambda: print(checkRadio.get()), textvariable = buttonStr)
button.pack()

checkVar = tk.BooleanVar()
check = ttk.Checkbutton(master = window, text = "Checkbox 1", command = lambda: print(checkVar.get()), variable = checkVar)
check.pack()


checkRadio = tk.IntVar()
radio1 = ttk.Radiobutton(master = window, text = 'Radiobutton 1', value = 1, variable = checkRadio, command = lambda: print(checkRadio.get()))
radio1.pack()
checkRadio2 = tk.IntVar()
radio2 = ttk.Radiobutton(master = window, text = 'Radiobutton 2', value = 2, variable = checkRadio, command = lambda: print(checkRadio.get()))
radio2.pack()

window.mainloop()