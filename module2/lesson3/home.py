# from tkinter import *
#
# window = Tk()
# window.geometry("400x250")
#
#
# class Image(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#         self.pack(fill=BOTH, expand=True)
#
#         canvas = Canvas(self)
#         canvas.create_line(10, 10, 100, 100, 150, 50, 10, 10 , fill="#1f1", width=2)
#         canvas.create_line(150, 10, 150, 100, 180, 200, 150, 10, fill="#2e2", width=2)
#         canvas.create_line(250, 110, 350, 150, 280, 200, 250, 110, fill="#2e2", width=2)
#
#         canvas.create_rectangle(230, 10, 290, 60, outline="#f11", fill="#1f1", width=2)
#         canvas.create_rectangle(20, 110, 90, 160, outline="#f11", fill="#1f1", width=2)
#         canvas.pack(fill=BOTH, expand=True)
#
#
# f = Image()
#
# window.mainloop()


import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, target):
        if type(self) == type(target):
            target.health -= 20
        else:
            raise TypeError


warriors = [Warrior('Воин 1'), Warrior('Воин 2')]
while True:
    user_choice = input('Введите 1, чтобы какой-то воин атаковал. Для закрытия программы введите 2: ')
    if user_choice == '1':
        i = random.randint(0, 1)
        attacker, victim = warriors[i], warriors[i - 1]
        attacker.hit(victim)
        print(attacker.name, 'атаковал', victim.name)
        print('У', victim.name, 'осталось здоровья', victim.health)
        if victim.health <= 0:
            print(attacker.name, 'победил!!!')
            break
    elif user_choice == '2':
        break
    else:
        print('Ошибка ввода')