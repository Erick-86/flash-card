from tkinter import *

root = Tk()
BACKGROUND_COLOR = "#B1DDC6"

root.title("Flash Card")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

root.mainloop()