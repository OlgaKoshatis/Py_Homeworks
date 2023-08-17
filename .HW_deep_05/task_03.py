#Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonac(a, b, d):
    fib_list = [a, b]
    for d in range(d):
        c = a + b 
        fib_list.append(c)
        a = b
        b = c
    return fib_list

n1 = int(input('Первое число:\t'))
n2 = int(input('Второе число:\t'))
n = int(input('Сколько чисел вывести:\t'))

print(fibonac(n1, n2, n))