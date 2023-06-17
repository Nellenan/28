import speech_recognition as sr
import random

# hello_list = ['И тебе привет!',
#               'Здравсвуйте!',
#               'Рада встрече!',
#               'Приветствую!',
#               'Мое почтение!']

film_list = ['Форсаж',
             'Трансформеры',
             'Человек-паук',
             'Кавказская пленница, или новые приключения Шурика',
             'Иван Васильевич меняет профессию']

recognizer = sr.Recognizer()
while True:
    with sr.Microphone(device_index=1) as source:
        print('Скажите что-нибудь...')
        audio = recognizer.listen(source)

        speech = recognizer.recognize_google(audio, language='ru_RU')

        print(f'Вы сказали: {speech}')

        if speech.lower() == 'фильм':
            print(random.choice(film_list))



