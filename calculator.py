import tkinter as tk

"""
Author: Jamey Kirk
Date: 05.20.2021
Class: CIS 112 - Calculator Project

Descirption: a simple calculator program that utiliizes tkinter for the GUI
"""

""" functions for calculations """

# converts num1 to negative value
def isNegative(x):
    
    if (num1.get()[0] == "-" and floatNum1.get() == True):
        return float(num1.get()[0:]) * -1
    elif (num1.get()[0] == "-"):
        return int(num1.get()[0:]) * -1

# completes calculations if both numbers are of type int
def calcInt():
    if(opperator.get() == "+"):
        calcView.set(int(num1.get()) + int(num2.get()))
    elif (opperator.get() == "-"):
        calcView.set(int(num1.get()) - int(num2.get()))
    elif (opperator.get() == "*"):
        calcView.set(int(num1.get()) * int(num2.get()))
    elif (opperator.get() == "/"):
        calcView.set(int(num1.get()) / int(num2.get()))

# completes calculations if any number is of type float
def calcFloat():
    if(opperator.get() == "+"):
        calcView.set(float(num1.get()) + float(num2.get()))
    elif (opperator.get() == "-"):
        calcView.set(float(num1.get()) - float(num2.get()))
    elif (opperator.get() == "*"):
        calcView.set(float(num1.get()) * float(num2.get()))
    elif (opperator.get() == "/"):
        calcView.set(float(num1.get()) / float(num2.get()))

# clears the calculator display
def clearView():
    num1.set("")
    num2.set("")
    opperator.set("")
    calcView.set(num1.get() + opperator.get() + num2.get())

# runs functions based on buttons entered into calculator
def btnFunctions(x):
    if (x == "clear"):
        clearView()

    elif (x == "="):
        if (isFloat.get()):
            calcFloat()
            isFloat.set(False)
        else:
            calcInt()

    # set num1, opperator, num2, and status of decimal point  
    else:
        if (x == "." and isFloat.get() == False and len(num2.get()) == 0):
            isFloat.set(True)
            floatNum1.set(True)
        elif (x == "." and isFloat.get() == False):
            isFloat.set(True)

        if (x == "+" and len(opperator.get()) == 0):
            opperator.set(x)
        elif (x == "-" and len(opperator.get()) == 0 and len(num1.get()) > 0):
            opperator.set(x)
        elif (x == "*" and len(opperator.get()) == 0):
            opperator.set(x)
        elif (x == "/" and len(opperator.get()) == 0):
            opperator.set(x)
        
        elif (len(opperator.get()) > 0):
            num2.set(num2.get() + x)
        else:
            num1.set(num1.get() + x)

        # displays everything on calculator
        calcView.set(num1.get() + opperator.get() + num2.get())

""" calculator GUI """

calcWindow = tk.Tk()
calcWindow.title("Calculator")

## global variables hold values for calculating, determining decimal count, and operator selection
num1 = tk.StringVar()
floatNum1 = tk.BooleanVar()
num2 = tk.StringVar()
opperator = tk.StringVar()
isFloat = tk.BooleanVar()
calcView = tk.StringVar()

## display frame and calculator output display
displayFrame = tk.Frame (calcWindow, width=400, height=250, bg="blue")
calcDispaly = tk.Entry(displayFrame, textvariable=calcView, bg="light blue", font=("Arial", "18"))

## button frame and buttons
# lambda functions enable values to be concatenated to number strings or applied to opperator variable
button1 = tk.Button (displayFrame, text="1", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("1"))
button2 = tk.Button (displayFrame, text="2", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("2"))
button3 = tk.Button (displayFrame, text="3", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("3"))
buttonPlu = tk.Button (displayFrame, text="+", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("+"))
button4 = tk.Button (displayFrame, text="4", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("4"))
button5 = tk.Button (displayFrame, text="5", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("5"))
button6 = tk.Button (displayFrame, text="6", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("6"))
buttonMin = tk.Button (displayFrame, text="-", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("-"))
button7 = tk.Button (displayFrame, text="7", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("7"))
button8 = tk.Button (displayFrame, text="8", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("8"))
button9 = tk.Button (displayFrame, text="9", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("9"))
buttonTim = tk.Button (displayFrame, text="*", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("*"))
button0 = tk.Button (displayFrame, text="0", height=2, width=20, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("0"))
buttonDot = tk.Button (displayFrame, text=".", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("."))
buttonDiv = tk.Button (displayFrame, text="/", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("/"))
buttonEqu = tk.Button (displayFrame, text="=", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("="))
buttonCle = tk.Button (displayFrame, text="Clear", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: btnFunctions("clear"))

## apply and layout frames and buttons to window
displayFrame.grid(row=0, column=3, rowspan=4, columnspan=6)
calcDispaly.grid(row=0, column=0, columnspan=6, ipady=8, ipadx=65)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
buttonPlu.grid(row=1, column=3)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
buttonMin.grid(row=2, column=3)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
buttonTim.grid(row=3, column=3)
button0.grid(row=4, column=0, columnspan=2, sticky="E, W")
buttonDot.grid(row=4, column=2)
buttonDiv.grid(row=4, column=3)
buttonEqu.grid(row=5, column=0, columnspan=3, sticky="E, W")
buttonCle.grid(row=5, column=3)

calcWindow.mainloop()