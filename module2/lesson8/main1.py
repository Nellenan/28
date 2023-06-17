from course import get_course, today
from tkinter import *

window = Tk()
window.geometry('500x500')
window.title('КиберБанк 2077')
window.resizable(width=False, height=False)
window.configure(background='yellow')

image = PhotoImage(file=r'C:\Users\Сергеев Никита\Desktop\Учёба\Python\module2\lesson8\logo.png')

label_img = Label(window, image=image, background='yellow')
label_img.place(x=0, y=0)

label_title = Label(window, text='КиберБанк', font='Arial 32', background='yellow')
label_title.place(x=150, y=55)
label_title = Label(window, text='2077', font='Arial 32', fg='#42AAFF', background='yellow')
label_title.place(x=380, y=55)

label_currency = Label(window, text=f'Курсы на {today}:', font='Arial 22', background='yellow')
label_currency.place(x=20, y=180)

dollar_info = f'{get_course("R01235").get("name")}: {get_course("R01235").get("value")}'
dollar_label = Label(window, text=dollar_info, font='Arial 18', background='yellow')
dollar_label.place(x=40, y=220)

euro_info = f'{get_course("R01239").get("name")}: {get_course("R01239").get("value")}'
euro_label = Label(window, text=euro_info, font='Arial 18', background='yellow')
euro_label.place(x=40, y=260)

uany_info = f'{get_course("R01375").get("name")}: {get_course("R01375").get("value")}'
uany_label = Label(window, text=uany_info, font='Arial 18', background='yellow')
uany_label.place(x=40, y=300)

entry = Entry(font='Arial 22')
entry.place(x=40, y=400)

y = 40


def search():
    global y

    currency_id = entry.get()
    currency_info = get_course(currency_id)

    currency_name = currency_info.get('name')
    currency_value = currency_info.get('value')

    currency_str = f'{currency_name} {currency_value}'
    currency_label = Label(window, text=currency_str, font='Arial 18', background='yellow')
    currency_label.place(x=40, y=300 + y)

    y += 40


button = Button(text='Найти', font='Arial 13', command=search)
button.place(x=370, y=403)


window.mainloop()
