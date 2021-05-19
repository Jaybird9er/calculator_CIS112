import tkinter as tk

window = tk.Tk()

frame = tk.Frame(window, width=300, height=300, bg="red")

btn1 = tk.Button(frame, text="button 1")
btn2 = tk.Button(frame, text="button 2")
btn3 = tk.Button(frame, text="button 3")
frame.pack()
btn1.pack(side=tk.LEFT, fill=tk.Y)
btn2.pack(side=tk.LEFT, fill=tk.Y)
btn3.pack(side=tk.LEFT, fill=tk.Y)

""" btn1.grid(row=0, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=2, column=2) """

window.mainloop()