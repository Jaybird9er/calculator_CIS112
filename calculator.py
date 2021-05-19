import tkinter as tk
from tkinter.constants import X

# functions for buttons
def digit1():
    pass


# calculator GUI

calcWindow = tk.Tk()
calcWindow.title("Calculator")

## display frame and output display
testFrame = tk.Frame (calcWindow, width=400, height=250, bg="sky blue")
displayFrame = tk.Frame (testFrame, width=370, height=50, bg="light blue")

## button frame and buttons
#buttonFrame = tk.Frame (calcWindow, height=250, width=400, bg="#55BBDD")
button1 = tk.Button (testFrame, text="1", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue")
button2 = tk.Button (testFrame, text="2", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue")
button3 = tk.Button (testFrame, text="3", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue")
buttonP = tk.Button (testFrame, text="+", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue")
button4 = tk.Button (testFrame, text="4", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue")

## layout frames and buttons
testFrame.grid(row=0, column=3, rowspan=4, columnspan=4)
displayFrame.grid(row=0, column=0, columnspan=4)
#buttonFrame.pack()
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
buttonP.grid(row=1, column=3)
button4.grid(row=2, column=0)


calcWindow.mainloop()