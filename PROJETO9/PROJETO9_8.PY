import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title = "Tabs"
window.geometry('600x400')

notebook = ttk.Notebook(window)
notebook.pack()

tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = "Text in tab1")
label1.pack()
button1 = ttk.Button(tab1, text = "Button1")
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = "Text in tab2")
label2.pack()
text1 = ttk.Entry(tab2)
text1.pack()

notebook.add(tab1, text = 'tab1') #notebooks must receive the frames as tabs with the .add method.
notebook.add(tab2, text = 'tab2')

window.mainloop()
