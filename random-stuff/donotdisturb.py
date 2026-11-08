import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()

#window configuration
root.title("Focus Up Device")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())
root.resizable(False,False)

root.mainloop()