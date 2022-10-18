#Kakulyator
what = input('Выбери действие (+, -, *, /): ')

a = float(input('Первое число: '))
b = float(input('Второе число: '))

if what == "+":
    c = a + b
    print('Ответ: ', c)
elif what == "-":
    c = a - b
    print('Ответ: ', c)
elif what == "*":
    c = a * b
    print('Ответ: ', c)
elif what == "/":
    c = a / b
    print('Ответ: ', c)
else:
    print('Ты по моему что-то перепутал!')

input()


