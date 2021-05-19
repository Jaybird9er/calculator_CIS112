import tkinter as tk

# functions for buttons
def digit1():
    pass


# calculator GUI

calcWindow = tk.Tk()
calcWindow.title("Calculator")

## display frame and output display
displayFrame = tk.Frame (calcWindow, height=50, width=390, bg="light blue")

## button frame and buttons
#buttonFrame = tk.Frame (calcWindow, height=250, width=400, bg="#55BBDD")
button1 = tk.Button (calcWindow, text="1", width=14, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue")
button2 = tk.Button (calcWindow, text="2", width=14, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue")
button3 = tk.Button (calcWindow, text="3", width=14, fg="blue", bg="#55BBDD", activeforeground="#55BBDD", activebackground="blue")

## layout frames and buttons
displayFrame.pack()
#buttonFrame.pack()
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)


calcWindow.mainloop()