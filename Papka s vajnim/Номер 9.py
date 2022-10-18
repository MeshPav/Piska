x = float(input("Первоначальный депозит")) 
x1 = x
y = 4
z = int(input("Колличество лет ")) 
 
for i in range (z):
    s = x / 100 * y 
    x += s 
    
print(int(x))