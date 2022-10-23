while True:
    x = int(input('Введите  магнитуду землятресения: '))
    if x <= 2:
        print('Минимальное')
    elif x <= 3:
        print('Очень слабое')
    elif x <= 4:
        print('Слабое')
    elif x <= 5:
        print('Промежуточное')
    elif x <= 6:
        print('Умеренное')
    elif x <= 7:
        print('Сильное!')
    elif x <= 8:
        print('Очень сильное!!')
    elif x <= 10:
        print('Огромное!!!')
    elif x > 10:
        print('Разрушительное!!!!')
