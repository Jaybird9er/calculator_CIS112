import tkinter as tk

# functions for buttons
def digit1():
    pass


# calculator GUI

calcWindow = tk.Tk()
calcWindow.title("Calculator")

## display frame and output display
displayFrame = tk.Frame (calcWindow, height=50, width=400, bg="light blue")

## button frame and buttons
buttonFrame = tk.Frame (calcWindow, height=250, width=400, bg="#55BBDD")


## layout frames and buttons
displayFrame.pack()
buttonFrame.pack()


calcWindow.mainloop()