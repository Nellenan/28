from tkinter import *

window = Tk()
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='white')
canvas.pack()

canvas.create_rectangle(150, 150, 400, 400, fill='green', outline='red')
canvas.create_polygon(150, 150, 275, 75, 400, 150, fill='purple', outline='red')


window.mainloop()