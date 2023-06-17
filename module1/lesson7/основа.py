from tkinter import *


facts = [
    {'text': 'Человеческое имя Халка - Брюс Беннет', 'right': 1},
    {'text': 'Уолт Дисней является создателем вселенной Marvel', 'right': 0},
    {'text': 'До появления костюма супергероя, человек муравей занимался воровством ', 'right': 1},
    {'text': 'Выдуманный город Дженоша является родиной Черной пантеры', 'right': 0}
]


window = Tk()
window.geometry('700x500')
window.title('Тестирование')

cur_q = 0
points = 0

def check():
    global cur_q, points

    answer = var.get()
    right_answer = facts[cur_q]['right']
    

    if answer == right_answer:
        points += 1

    if cur_q < len(facts) - 1:
        cur_q += 1
        message['text'] = facts[cur_q]['text']
    else:
        points_label = Label(text='Вы набрали: ' + str(points) + ' очко/очка', font=('Arial', 24),
        fg='white', bg='red')
        points_label.place(x=0, y=0, width=700, height=500)

label_title = Label(
    text='Тестирование по вселенной Marvel',
    font=('Arial', 24),
    bg='red',
    fg='white'
)

label_title.place(x=0, y=0, width=700, height=50)

message = Message(text=facts[cur_q]['text'], font=('Ariel', 18), width=680)
message.place(x=10, y=100)

var = IntVar()

true = Radiobutton(text='Правда', variable=var, value=1)
true.place(x=10, y=150)

false = Radiobutton(text='Ложь', variable=var, value=0)
false.place(x=10, y=200)

button = Button(text= 'Ответить', command=check)
button.place(x=10, y=230)



window.mainloop()

















