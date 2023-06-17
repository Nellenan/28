#1

# from tkinter import *



# window = Tk()
# window.geometry('700x500')
# window.title('Лотерея nescam.com')

# label = Label(text='!!!!!!!!ВЫ ВЫЙГРАЛИ В ЛОТЕРЕЕ!!!!!!', font=('Ariel', 24), fg='black', bg='yellow' )
# label.place(x=0, y=0, width=700, height=500)

# def check():
#     global button
#     if Button == 'ПОЛУЧИТЬ ВЫЙГРЫШ':
#         but['text'] = 'Чтобы забрать выйгрыш необходимо внести 1000руб.'
#     else:
#         but['text'] = 'ПОЛУЧИТЬ ВЫЙГРЫШ'
        



# but = Button(text='ПОЛУЧИТЬ ВЫЙГРЫШ', command=check)
# but.place(x=270, y=300)
# window.mainloop()


# 2


# dogs = int(input())
# lst = list()

# for i in range(dogs): lst.append(int(input()))
# print(lst)

# points_min = min(lst)
# ind_min = lst.index(points_min)
# points_max = max(lst)
# ind_max = lst.index(points_max)
# lst[ind_min] = points_max
# lst[ind_max] = points_min

# print(lst)


# 3

from tkinter import *
import time
 
window = Tk()
window.geometry('1280x750')
window.title('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DANGEROUS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
window.resizable(width=False, height=False)
count = 5


def on_close():
    global count
    if count > 0:
        label['text'] = count
        count -= 1
        window.after(500, on_close)
    else:
        time.sleep(3)
        screen_wight = window.winfo_screenwidth()
        screen_heihgt = window.winfo_screenheight()
        photo = PhotoImage(file='cow.gif')
        window.geometry(str(screen_wight) + 'x' + str(screen_heihgt))
        label['image'] = photo
        label.image = photo
        label.place(x=0, y=0, width=screen_wight, height=screen_heihgt)

label = Label(text='Внимаиние угроза - польская корова, срочно закройте это окно', font=('Arial, 24'), fg='red', bg='black')
label.place(x=0, y=0, width=1280, height=750)

window.protocol('WM_DELETE_WINDOW', on_close)


window.mainloop()



