n = int(input("Введите число "))
a1 = 0
while(n > 0):
    a2 = n % 10
    a1 = a1 + a2
    n = n//10
print("Ответ ", a1)