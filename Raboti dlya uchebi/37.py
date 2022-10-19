spysok = [['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], ['Y', 'y']]
# spysok.sort()
# spysok.append('y')
# spysok.append('Y')
# spysok.sort()
g = 'Это гласная буква'
s = 'Это согласная буква'
y = 'Эта буква может быть как гласной, так и согласной'
while True:
    a = input('Введите латинскую букву: ')
    if a in spysok[0]:
        print(g)  # Это гласная буква
    elif a in spysok[1][0] or a in spysok[1][1]:
        print(y) #Эта буква может быть как гласной, так и согласной
    else:
        print(s) #Это согласная буква
    if input(f'Продолжить? [Да/Нет] \n') != 'Да': break
