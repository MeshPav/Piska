import keyboard
import time
import random

red_num = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_num = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
chet_num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
nechet_num = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
zero_num = [0]
doublezero_num = [37]
first_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, ]
second_num = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
while True:
    color = ''
    chet = ''
    nums = ''
    c = ''
    a = input('**Пришло время сделать вашу ставку** \n Возможные ставки: \n '
              'Чёрное-Красное \n '
              'Чётное-Нечётное \n '
              '1-18 // 19-36 \n '
              '00 \n '
              'Любое число от 0 до 36 \n')
    b = random.randint(0, 38)
    print('Выпавшее число: ', b)
    if b in red_num:
        print('Выигрышная ставка: Красное')
        color = 'красное'
    if b in black_num:
        print('Выигрышная ставка: Чёрное')
        color = 'чёрное'
    if b in chet_num:
        print('Выигрышная ставка: Чётное')
        chet = 'Чётное'
    if b in nechet_num:
        print('Выигрышная ставка: Нечётное')
        chet = 'Нечётное'
    if b in first_num:
        print('Выигрышная ставка: 1-18')
        nums = '1-18'
    if b in second_num:
        print('Выигрышная ставка: 19-36')
        nums = '19-36'
    if b in zero_num:
        print('Выигрышная ставка: 0')
    if b in doublezero_num:
        print('Выигрышная ставка: 00')
    time.sleep(1)
    print('Перезапустить рулетку? [y/n] ')
    key = keyboard.read_key()
    if key not in ('y', 'n'):
        if key != 'y' or 'n':
            print('Неправильная кнопка, до свидания ')
            time.sleep(1)
            break
    else:
        if key == 'y':
            time.sleep(1)
            continue
        else:
            time.sleep(1)
            print('До свидания')
            break
