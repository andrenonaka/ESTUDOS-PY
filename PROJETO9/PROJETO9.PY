import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mileInput = entryInt.get()
    kmOutput = mileInput*1.61
    outputString.set(kmOutput)

#window
window = ttk.Window(themename = 'darkly') #create basic window
window.title('Test') #give the window a header title
window.geometry('300x150') #set window size

#title
titleLabel = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold') #create a label (for text), set its master container (window var) and the text
titleLabel.pack() #places label widget in window

#input field
inputFrame = ttk.Frame(master = window) #container for entry box and button
entryInt = tk.IntVar() #This var is a bridge between GUI and Python code
entry = ttk.Entry(master = inputFrame, textvariable = entryInt) #textvariable indicates the var that will receive the text from entry
button = ttk.Button(master = inputFrame, text = 'Convert', command = convert)
#IMPORTANT: the function "convert" in "command" is only passed, not called. The button will call the function when pressed. 

entry.pack(side = 'left', padx = 10) #packs entry box into inputFrame - padx and pady adds padding the widgted in the x and y axis.
button.pack(side = 'left') #packs button into inputFrame
inputFrame.pack(pady = 10) #packs inputFrame into window

#output
outputString = tk.StringVar() #This var will hold the data for the label
outputLabel = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = outputString)
#textvariable indicates the var that will receive the text for label. Overrides text.
outputLabel.pack(pady = 10)

#OBS: .pack() funtions place the widgets on from top to bottom in the order they appear in code.

#run
window.mainloop()