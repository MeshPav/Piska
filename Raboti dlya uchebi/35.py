while True:
    a = int(input("Введите целое число: "))
    if a % 2 == 0:
        print(f"Число '{a}' чётное")
    else:
        print(f"Число '{a}' не чётное")
    if input(f'Продолжить? [Да/Нет] \n') != 'Да': break
