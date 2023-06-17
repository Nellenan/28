from tkinter import *
import random


window = Tk()
window.geometry('600x600')

canvas = Canvas(window, width=600, height=600)
canvas.pack()

background = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module2\lesson4\bg_2.png')


class Knight:
    def __init__(self):
        self.x = 150
        self.y = 350
        self.vy = 0
        self.vx = 0
        self.photo = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module2\lesson4\knight.png')

    def up(self, event):
        self.vy = -3

    def down(self, event):
        self.vy = 3

    def stop(self, event):
        self.vx = 0
        self.vy = 0

    def right(self, event):
        self.vx = 3

    def left(self, event):
        self.vx = -3


knight = Knight()


class Dragon:
    def __init__(self):
        self.x = random.randint(550, 600)
        self.y = random.randint(50, 550)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module2\lesson4\dragon.png')


dragons = []
for i in range(5):
    dragons.append(Dragon())


def game():
    canvas.delete('all')
    canvas.create_image(300, 300, image=background)
    canvas.create_image(knight.x, knight.y, image=knight.photo)

    for dragon in dragons:
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        dragon.x -= dragon.v

        if ((knight.x - dragon.x) ** 2 + (knight.y - dragon.y) ** 2) ** 0.5 < 50:
            dragons.remove(dragon)

        if dragon.x < 50:
            lose()

    if knight.y < 30 or knight.y > 600:
        knight.vy = -knight.vy

    if knight.x < 30 or knight.x > 600:
        knight.vx = -knight.vx

    knight.x += knight.vx
    knight.y += knight.vy
    print(knight.x, knight.y)

    if len(dragons) == 0:
        return win()

    window.after(10, game)


def win():
    canvas.create_text(300, 300, text='Вы победили!', font='Verdana 42')


def lose():
    canvas.create_text(300, 300, text='Вы проиграли', font='Verdana 42')


window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)


game()
window.mainloop()




