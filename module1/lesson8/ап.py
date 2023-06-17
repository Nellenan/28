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
        photo = PhotoImage(file='cow.jpg')
        window.geometry(str(screen_wight) + 'x' + str(screen_heihgt))
        label['image'] = photo
        label.image = photo
        label.place(x=0, y=0, width=screen_wight, height=screen_heihgt)

label = Label(text='Внимаиние угроза - польская корова, срочно закройте это окно', font=('Arial, 24'), fg='red', bg='black')
label.place(x=0, y=0, width=1280, height=750)

window.protocol('WM_DELETE_WINDOW', on_close)


window.mainloop()