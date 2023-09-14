# Напишите следующие функции:

# - Нахождение корней квадратного уравнения
# - Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# - Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# - Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

from random import randint
import csv
import math

from decoration import discr_in_csv_decor, write_in_json


# Запись CSV FILE с тремя случайными числами в каждой строке
def csv_write(name_csv_file: str, count_rows: int):
    with open(name_csv_file + '.csv', 'w', newline='', encoding='utf-8') as f:
        file_csv = csv.writer(f)
        for _ in range(1, count_rows + 1):
            k = []
            for _ in range(1, 4):
                k.append(randint(1, 9))
            file_csv.writerow(k)
    print(f'Запись значений в формат CSV прошла успешно')

# Чтение CSV FILE
def csv_read(name_csv_file):
    with open(name_csv_file + '.csv', 'r', newline='', encoding='utf-8') as f:
        file_csv = csv.reader(f, delimiter=',')
        for i in file_csv:
            print(i)
# csv_read('file')


# Декоратор поиска корней из значений файла CSV
# Декоратор записи в файл JSON
@write_in_json
@discr_in_csv_decor
# функция поиска корней дискриминанта
def roots_discr(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return f'Корни дискриминанта: x1 = {round(x1, 1)}, x2 = {round(x2, 1)}'

    elif discr == 0:
        x = -b / (2 * a)
        return f'Корень дискриминанта: x = {round(x, 2)}'
    else:
        return "Корней нет"


csv_write('file_random_number', 100)
roots_discr('json_file_roots_discr', 'file_random_number')