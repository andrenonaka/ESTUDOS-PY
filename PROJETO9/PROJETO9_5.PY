import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Exercício RadioCheck Buttons')
window.geometry('400x200')

checkVar = tk.BooleanVar()
checkButton = ttk.Checkbutton(window, text = 'Check Button', variable = checkVar, command = lambda: print(radioVar.get()))
checkButton.pack()

def radio_button_press():
    print(checkVar.get())
    checkVar.set(False)

radioVar = tk.StringVar()
radioButton1 = tk.Radiobutton(window, text = 'Radio Button 1', value = 'A', variable = radioVar, command = radio_button_press)
radioButton1.pack()

radioButton2 = tk.Radiobutton(window, text = 'Radio Button 2', value = 'B', variable = radioVar, command = radio_button_press)
radioButton2.pack()

window.mainloop()