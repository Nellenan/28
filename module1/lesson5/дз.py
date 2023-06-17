




#1
questions = [{'question': 'Кто из героев Киновселенной Marvel начал знакомство с Землёй, попав под грузовик?',
              'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'], 'right_answer': 4},
             {'question': 'Как звучит полное имя младшего брата Тора?',
              'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
              'right_answer': 3}, 
              {'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
                 'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'], 'right_answer': 1},
                 {'question': 'В каком из перечисленный фильмов Тор появился раньше?', 'answers':['Мстители.Финал','Тор Рагнарёк', 'Мстители','Тор'],'right_answer': 4}]

score = 0

for i_question in questions:
    question_text = i_question.get("question")
    answers = i_question.get("answers")
    right_answer = i_question.get("right_answer")
    
    print (question_text)
    length_of_list_with_answers = len(answers)
    for answer in range(length_of_list_with_answers):
        print(answer + 1, answers[answer])

        user_answer = int(input('Введите номер ответа: '))
        
    if user_answer == right_answer:
         print('Верно, + 1 очко')
         score += 1
    else:
        print('Неверно, + 0 очков')

if  score >= 3:
    print('Ты победил!','Твой счёт: ', score)
else:
    print('Ты проиграл.','Твой  счёт: ', score)




#2

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count = int(input('Сколько песен выбрать? '))
all_time = 0.0

for i in range(count):
    user_query = f'Название {i + 1} песни: '
    song_name = input(user_query)
    all_time += violator_songs.get(song_name, 0)
 
print(f'Общее время звучания песен: {round(all_time, 2)} минут')





#3

for name,code in goods.item():
    product_info = store.get(code)
    summa = 0
    for i_item in product_info:
        quantity = i_item.get('quantity')
        price = i_item.get('price')

        summa += quantity * price
    print(name, summa)


