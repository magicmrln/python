import tkinter as tk
from tkinter import ttk


# functions
def calculateResult():
    global result
    global operation
    x = num1.get()
    y = num2.get()
    calculation = f"{x}{operation.get()}{y}"
    result = f"{eval(calculation):.2f}"
    resultDisplay.config(text=result)


# window
window = tk.Tk()

window.title("Calculator")
window.geometry("400x100")
window.minsize(400, 100)

# window elements
title = ttk.Label(master=window, text="Calculator", font="Arial 20 bold")
title.pack(pady=2)

result = 0
operations = ["+", "-", "*", "/"]
operation = tk.StringVar(value="+")

frame1 = ttk.Frame(master=window)
num1 = ttk.Entry(master=frame1, width=10)
operationGui = ttk.OptionMenu(frame1, operation, "+", *operations)
num2 = ttk.Entry(master=frame1, width=10)
equalSymbol = ttk.Label(master=frame1, text="=")
resultDisplay = ttk.Label(master=frame1, text=result)
calculateButton = ttk.Button(master=frame1, text="calculate", command=calculateResult)

num1.pack(side="left", padx=5)
operationGui.pack(side="left", padx=5)
num2.pack(side="left", padx=5)
equalSymbol.pack(side="left", padx=5)
resultDisplay.pack(side="left", padx=10)
calculateButton.pack(side="left")
frame1.pack(pady=6)


# run
window.mainloop()
