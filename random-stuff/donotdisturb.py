import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()

#window configuration
root.title("Focus Up Device")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())
root.resizable(False,False)
root.configure(bg="black")

label1 = tk.Label(root, text="Welcome! This is a window so that you can keep focus.", font=("Comic Sans MS", 50, "bold"), bg="black")
label2 = tk.Label(root, text="Please enter the number of minutes you will be using this window:", font=("Comic Sans MS", 50, "bold"), bg="black")
minutesUsing = tk.IntVar()
minuteEntryBox = ttk.Entry(root, textvariable=minutesUsing, width=40, font=("Comic Sans MS", 50), justify="center")




label1.pack()
label2.pack()
minuteEntryBox.pack()
root.mainloop()