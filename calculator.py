import tkinter as tk

""" 
To Do:

1. Create functions for each button
2. Create functions for the clear button to clear reset any function
3. Apply values for num1 and num2 globaly depending on state of calculation
4. Limit decimal stroke so it only applies one time to each value
5. All values (num1, num2, arithmetic operators) should be displayed in string form in the calculator display
6. Need global variables to determine num1, num2, decimal, and operator states
7. All calulations are conducted using Lambda Functions (num1 and num2 are stored in functions) and can be cleared at anytime
"""

## functions for calculations
def getNum1():
    global num1
    return num1

def numbers(x):
    if (x == "clear"):
        num1.set("")
        num2.set("")
        opperator.set("")
        calcView.set(num1.get() + opperator.get() + num2.get())

    elif (x == "="):
        if(opperator.get() == "+"):
            calcView.set(sum((int(num1.get()), int(num2.get()))))
    else:
        if (x == "+" and len(opperator.get()) == 0):
            opperator.set(x)
        elif (len(opperator.get()) > 0):
            num2.set(num2.get() + x)
            print(num2.get())
        else:
            num1.set(num1.get() + x)
            print(num1.get())
    
        calcView.set(num1.get() + opperator.get() + num2.get())


## functions for calculator buttons
def digit1():
    global num1
    global num2
    #if 
    num1.set(num1.get() + "1")

def digit2():
    global num2
    num2.set(num2.get() + "2")

def plusBtn():
    global opperator
    opperator.set("+")

def equalBtn():
    print(int(num1.get()), len(num1.get()), type(num1.get()), type(int(num1.get())))

"""
May need to use one variable for the dispaly and have it copied into 
another varible within the functions to convert it to a float value

Seems very complicated, but can't think of a better way at the moment
"""


calcWindow = tk.Tk()
calcWindow.title("Calculator")

## global variables hold values for calculating, determining decimal count, and operator selection
num1 = tk.StringVar()
num2 = tk.StringVar()
opperator = tk.StringVar()
calcView = tk.StringVar()


if(type(num1.get()) != type("")):
    print(int(num1.get()))

print(type(num1.get()))
print(type(""))
print(len(opperator.get()))

## calculator GUI

## display frame and calculator output display
displayFrame = tk.Frame (calcWindow, width=400, height=250, bg="blue")
calcDispaly = tk.Entry(displayFrame, textvariable=calcView, bg="light blue", font=("Arial", "18"))

## button frame and buttons
button1 = tk.Button (displayFrame, text="1", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: numbers("1"))
button2 = tk.Button (displayFrame, text="2", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: numbers("2"))
button3 = tk.Button (displayFrame, text="3", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
buttonPlu = tk.Button (displayFrame, text="+", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: numbers("+"))
button4 = tk.Button (displayFrame, text="4", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
button5 = tk.Button (displayFrame, text="5", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
button6 = tk.Button (displayFrame, text="6", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
buttonMin = tk.Button (displayFrame, text="-", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
button7 = tk.Button (displayFrame, text="7", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
button8 = tk.Button (displayFrame, text="8", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
button9 = tk.Button (displayFrame, text="9", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
buttonTim = tk.Button (displayFrame, text="*", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
button0 = tk.Button (displayFrame, text="0", height=2, width=20, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
buttonDot = tk.Button (displayFrame, text=".", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
buttonDiv = tk.Button (displayFrame, text="/", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
# may be able to apply lambda function in the command(lambda num1 opp num2: num1 opp num2)
buttonEqu = tk.Button (displayFrame, text="=", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: numbers("="))
buttonCle = tk.Button (displayFrame, text="Clear", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"), command=lambda: numbers("clear"))

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