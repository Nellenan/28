questions = [{'question': 'Кто из героев Киновселенной Marvel начал знакомство с Землёй, попав под грузовик?',
              'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'], 'right_answer': 4},
             {'question': 'Как звучит полное имя младшего брата Тора?',
              'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
              'right_answer': 3}, 
              {'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
                 'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'], 'right_answer': 1},
                 {'question': 'В каком из перечисленный фильмов Тор появился раньше?', 'answers':['Мстители.Финал','Тор Рагнарёк', 'Мстители','Тор'],'right_answer': 4}]

name = input('Введите ваше: ')



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

result = open('test.txt', 'a', encoding='utf-8')
result.write('Результат теста пользователя ' + name + str(score) + '/n')


