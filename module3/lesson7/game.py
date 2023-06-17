from  tkinter import *
import random

window = Tk()
window.geometry('600x600')
window.title('Алхимия')


class Pottery:
    image = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module3\lesson7\pottery.png').subsample(4, 4)


class Steam:
    image = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module3\lesson7\aroma.png').subsample(4, 4)


class Dust:
    image = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module3\lesson7\dust.png').subsample(4, 4)


class Water:
    image = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module3\lesson7\water.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, FIre):
            return Steam


class FIre:
    image = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module3\lesson7\fire.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam
        elif isinstance(other, Ground):
            return Pottery


class Wind:
    image = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module3\lesson7\wind.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Ground):
            return Dust


class Ground:
    image = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module3\lesson7\ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust
        elif isinstance(other, FIre):
            return Pottery

canvas = Canvas(height=600, width=600)
canvas.pack()

elements = [Wind(), FIre(), Water(), Ground()]

for elem in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)


def move(event):
    images_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_ids) == 2:
        elem_id_1, elem_id_2 = images_ids[0], images_ids[1]
        elem_1 = elements[elem_id_1 - 1]
        elem_2 = elements[elem_id_2 - 1]

        new_elem = elem_1 + elem_2
        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)
    canvas.coords(images_ids, event.x, event.y)


window.bind('<B1-Motion>', move)

window.mainloop()
