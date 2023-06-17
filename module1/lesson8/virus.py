from tkinter import *


window = Tk()
window.geometry('700x500')
window.title('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DANGEROUS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
window.resizable(width=False, height=False)
count = 5


def on_close():
    global count
    if count > 0:
        label['text'] = count
        count -= 1
        window.after(1000, on_close)
    else:
        screen_wight = window.winfo_screenwidth()
        screen_heihgt = window.winfo_screenheight()
        photo = PhotoImage(file='skelet.gif')
        window.geometry(str(screen_wight) + 'x' + str(screen_heihgt))
        label['image'] = photo
        label.image = photo
        label.place(x=0, y=0, width=screen_wight, height=screen_heihgt)


label = Label(text='Ваш компьютор заражён!!!!!!!111!!1!!!1', font='Arial 24', fg='red', bg='black')
label.place(x=0, y=0, width=700, height=500)


window.protocol('WM_DELETE_WINDOW', on_close)


window.mainloop()


# pip instal pyinstaller
# pyinstaller -F -i 'virus.ico' virus.py









































