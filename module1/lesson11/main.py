from fpdf import FPDF
from datetime import datetime


pdf = FPDF('P','mm', 'A4')
pdf.add_page()
pdf.set_right_margin(50)
pdf.set_left_margin(50)
pdf.image('bg.jpg', x=0, y=0, w=210, h=297)
pdf.add_font('comic', '', 'C:\WINDOWS\FONTS\COMIC.ttf', uni=True)
pdf.set_font('comic', size=18)


name = input('Кому открытка? ')
pdf.set_text_color(148, 86, 235)
pdf.cell(w=0, h=90, ln=1)
pdf.cell(w=0, h=20, txt='Дорогой(ая), ' + name + '!', align='C', ln=1)


text = input('Введите текст поздравления: ')
pdf.multi_cell(w=0, h=15, txt=text, align='C')


today = datetime.today().strftime('%d.%m.%Y')
pdf.cell(w=0, h=25, txt=today, align='R')


from_ = input('От кого открытка? ')
pdf.cell(w=0, h=40, txt=from_,align='R')


pdf.output('birth.pdf')