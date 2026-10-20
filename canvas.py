import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
C = tk.Canvas(top, bg="pink", height=350, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=360, extent=150, fill="black")
C.pack()
top.mainloop()