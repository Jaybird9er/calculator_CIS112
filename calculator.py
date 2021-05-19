import tkinter as tk
from tkinter.constants import E, W, X

# functions for buttons
def digit1():
    pass


# calculator GUI

calcWindow = tk.Tk()
calcWindow.title("Calculator")

## display frame and output display
displayFrame = tk.Frame (calcWindow, width=400, height=250, bg="blue")
holdFrame = tk.Frame (displayFrame, width=360, height=50, bg="light blue")

## button frame and buttons
#buttonFrame = tk.Frame (calcWindow, height=250, width=400, bg="#55BBDD")
button1 = tk.Button (displayFrame, text="1", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
button2 = tk.Button (displayFrame, text="2", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
button3 = tk.Button (displayFrame, text="3", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
buttonPlu = tk.Button (displayFrame, text="+", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
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
buttonEqu = tk.Button (displayFrame, text="=", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))
buttonCle = tk.Button (displayFrame, text="Clear", height=2, width=10, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue", font=("Arial", "16"))

## layout frames and buttons
displayFrame.grid(row=0, column=3, rowspan=4, columnspan=6)
holdFrame.grid(row=0, column=0, columnspan=4)
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
button0.grid(row=4, column=0, columnspan=2, sticky=E+W)
buttonDot.grid(row=4, column=2)
buttonDiv.grid(row=4, column=3)
buttonEqu.grid(row=5, column=0, columnspan=3, sticky=E+W)
buttonCle.grid(row=5, column=3)


calcWindow.mainloop()