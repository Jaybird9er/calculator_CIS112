import tkinter as tk

"""
Author: Jamey Kirk
Date: 05.20.2021

To Do:

1. Create functions for each button
2. Create functions for the clear button to clear reset any function
3. Apply values for num1 and num2 globaly depending on state of calculation
4. Limit decimal stroke so it only applies one time to each value
5. All values (num1, num2, arithmetic operators) should be displayed in string form in the calculator display
6. Need global variables to determine num1, num2, decimal, and operator states
7. All calulations are conducted using Lambda Functions (num1 and num2 are stored in functions) and can be cleared at anytime
"""

""" functions for calculations """

# converts value to negative value
def isNegative(x):
    pass
    # num1
    # if (num1.get()[0] == "-"):
    #     return int(num1.get()[0:]) * -1
    # elif (num2.get()[0] == "-"):
    #     return int(num2.get()[0:]) * -1

    # if (negNum1.get() == True and floatNum1.get() == True):
    #     print("A")
    #     return (float(num1.get()[0:]) * -1)
    # elif(negNum1.get() == True and floatNum1.get() == False):
    #     print("B")
    #     return int(num1.get()[0:]) * -1
    # elif(negNum1.get() == False and floatNum1.get() == True):
    #     print("C")
    #     return float(num1.get())
    # elif(negNum1.get() == False and floatNum1.get() == False):
    #     print("D")
    #     return int(num1.get())
    # # num2
    # if (negNum2.get() == True and floatNum2.get() == True):
    #     print("E")
    #     return float(num2.get()[1:]) * -1
    # elif(negNum2.get() == True and floatNum2.get() == False):
    #     print("F")
    #     return int(num2.get()[1:]) * -1
    # elif(negNum2.get() == False and floatNum2.get() == True):
    #     print("G")
    #     return float(num2.get())
    # elif(negNum2.get() == False and floatNum2.get() == False):
    #     print("H")
    #     return int(num2.get())


# completes calculations if numbers are of type int
# def calcInt():
#     if(opperator.get() == "+"):
#         calcView.set(isNegative(num1.get()) + isNegative(num2.get()))
#     elif (opperator.get() == "-"):
#         calcView.set(isNegative(num1.get()) - isNegative(num2.get()))
#     elif (opperator.get() == "*"):
#         calcView.set(isNegative(num1.get()) * isNegative(num2.get()))
#     elif (opperator.get() == "/"):
#         calcView.set(isNegative(num1.get()) / isNegative(num2.get()))

# completes calculations if numbers are of type int
def calcInt():
    if(opperator.get() == "+"):
        calcView.set(int(num1.get()) + int(num2.get()))
    elif (opperator.get() == "-"):
        calcView.set(int(num1.get()) - int(num2.get()))
    elif (opperator.get() == "*"):
        calcView.set(int(num1.get()) * int(num2.get()))
    elif (opperator.get() == "/"):
        calcView.set(int(num1.get()) / int(num2.get()))

# completes calculations if numbers are of type float
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
        if (floatOrInt.get()):
            calcFloat()
            floatOrInt.set(False)
        else:
            calcInt()

    # set num1, opperator, num2, and status of decimal point  
    else:
        if (x == "." and floatOrInt.get() == False):
            floatOrInt.set(True)

        if (x == "+" and len(opperator.get()) == 0):
            opperator.set(x)
        elif (x == "-" and len(opperator.get()) == 0 and len(num1.get()) > 0):
            opperator.set(x)
        elif (x == "*" and len(opperator.get()) == 0):
            opperator.set(x)
        elif (x == "/" and len(opperator.get()) == 0):
            opperator.set(x)

        # elif (len(num1.get()) == 0 and x == "-" and len(opperator.get()) == 0):
        #     negNum1.set(True)
        # elif (len(num2.get()) == 0 and x == "-" and len(opperator.get()) == 1):
        #     negNum2.set(True)

        # elif (x == "." and floatNum1.get() == False):
        #     floatNum1.set(True)
        # elif (x == "." and floatNum2.get() == False):
        #     floatNum2.set(True)
        
        elif (len(opperator.get()) > 0):
            num2.set(num2.get() + x)
            print(num2.get())
        else:
            num1.set(num1.get() + x)
            print(num1.get())
        # displays everything on calculator
        calcView.set(num1.get() + opperator.get() + num2.get())


# ## functions for calculator buttons
# def digit1():
#     global num1
#     global num2
#     #if 
#     num1.set(num1.get() + "1")

# def digit2():
#     global num2
#     num2.set(num2.get() + "2")

# def plusBtn():
#     global opperator
#     opperator.set("+")

# def equalBtn():
#     print(int(num1.get()), len(num1.get()), type(num1.get()), type(int(num1.get())))

"""
May need to use one variable for the dispaly and have it copied into 
another varible within the functions to convert it to a float value

Seems very complicated, but can't think of a better way at the moment
"""

""" calculator GUI """

calcWindow = tk.Tk()
calcWindow.title("Calculator")

## global variables hold values for calculating, determining decimal count, and operator selection
num1 = tk.StringVar()
negNum1 = tk.BooleanVar()
floatNum1 = tk.BooleanVar()
num2 = tk.StringVar()
negNum2 = tk.BooleanVar()
floatNum2 = tk.BooleanVar()
opperator = tk.StringVar()
floatOrInt = tk.BooleanVar()
calcView = tk.StringVar()


if(type(num1.get()) != type("")):
    print(int(num1.get()))

print(type(num1.get()))
print(type(""))
print(len(opperator.get()))


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

## layout frames and buttons
displayFrame.grid(row=0, column=3, rowspan=4, columnspan=6)
#calcFrame.grid(row=0, column=0, columnspan=6, sticky="N, S, E, W")
calcDispaly.grid(row=0, column=0, columnspan=6, ipady=8, ipadx=65)
#buttonFrame.pack()
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