from tkinter import *

root = Tk()
canvas = Canvas(root, width=1000, height=1000, bg='white')
canvas.pack()

wSize = 1000
radius = 400

def drawCircle(x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, width=1)

    if r >= 5:
        drawCircle(x-r//2, y, r//2)
        drawCircle(x+r//2, y, r//2)

drawCircle(wSize//2, wSize//2, radius)


root.mainloop()