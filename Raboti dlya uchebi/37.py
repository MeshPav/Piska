spysok = [['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'], ['Y', 'y']]
# spysok.sort()
# spysok.append('y')
# spysok.append('Y')
# spysok.sort()
g = 'Это гласная буква'
s = 'Это согласная буква'
y = 'Может быть как гласной, так и согласной'
while True:
    a = input('Введите латинскую букву: ')
    if a in spysok[0]:
        print(f"Буква '{a}' " + g) # Буква 'a' Это гласная буква
    elif a in spysok[1][0] or a in spysok[1][1]:
        print(f"Буква '{a}' " + y) #Буква 'a' Может быть как гласной, так и согласной
    else:
        print(f"Буква '{a}' " + s) # Буква 'a' Это согласная буква
    if input(f'Продолжить? [Да/Нет] ') != 'Да': break
