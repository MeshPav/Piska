f = int(input("Введите кол-во футов: "))
d = int(input("Введите кол-во дюймов: "))
d += f * 12
cm = round(d * 2.54, 1)
print("Рост : %d см." % cm)
