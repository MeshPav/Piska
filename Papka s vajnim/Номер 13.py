summa = int(input('Сдача '))
monetki = [25, 10, 5, 1]
for a in monetki:
    res, summa = divmod(summa, a)
    if res:
        print(f'{a} - {res}')