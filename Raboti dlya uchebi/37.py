a = input("Введите  букву латинского алфавита ")
spisok = ["a", "e", "i", "o", "u"]
if a in spisok:
  print(f"буква {a} гласная")
elif a == 'y':
  print(f"буква '{a}' может быть как гласной, так и согласной")
else:
  print("введена согласная буква")