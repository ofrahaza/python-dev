
questions = ['Какая версия языка сейчас актуальна?',
             'Какая кодировка используется в строках?',
             'Сколько значений есть у bool?',
             'Код b’a1b2c3’ валиден?',
             'Зачем используются операторы `in` и `not in` со строками?',
             'Какой метод создает новую строку с символам в нижнем регистре?',
             'Какой метод создает новую строку с символам в верхнем регистре?',
             'Сколько байт выделяется в utf-8 для ASCII символов?',
             'Как взять последний символ строки my_str?',
             'Какую кодировку нужно использовать по умолчанию?'
             ]

answers = ['python3',
           'utf8',
           '2',
           'да',
           'для проверки вхождения подстроки',
           'lower()',
           'upper()',
           '1',
           'my_str[-1]',
           'utf8'
           ]

correct = 0
incorrect = 0

for (index, element) in enumerate(questions):
    print(element)
    answer = input('Введите ответ: ')

    if answer.lower() == answers[index]:
        print('Верно!')
        correct += 1
    else:
        print(f'Неверно! Верный ответ: {answers[index]}')
        incorrect += 1

print('Верных ответов {0}, неверных ответов: {1}'.format(correct, incorrect))