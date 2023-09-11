#Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def gen_fibonacci(x: int, y: int, z: int):
    
    for i in range(z):
        yield x
        x, y = y, x + y

x = in
t(input("Первое число: "))
y = int(input("Второе число: "))
z = int(input("Какое количество чисел вывести: "))

for num in gen_fibonacci(x, y, z):
    print(num)