#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

n = int(input('Введите число: \n'))
res = []
for i in range(1, n+1):
    while n > 15:
        res.insert(0, n % 16)
        n = n//16
        i += 1
if n < 16:
    res.insert(0, n)

hex_string = '0x'
for el in res: 
    if el < 10:
        hex_string += str(el)
    elif el == 10:
        hex_string += str('A')
    elif el == 11:
        hex_string += str('B')
    elif el == 12:
        hex_string += str('C')
    elif el == 13:
        hex_string += str('D')
    elif el == 14:
        hex_string += str('E')
    elif el == 15:
        hex_string += str('F')

print(hex_string)


