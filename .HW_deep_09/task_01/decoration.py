import csv
import json


# Декоратор преобразующий в словарь корни квадратного
# уравнения с каждой тройкой чисел из csv файла
def discr_in_csv_decor(func):
    dict_file = {}
    def wrapper(file_name, *args, **kwargs):
        with open(file_name + '.csv', 'r', newline='', encoding='utf-8') as f:
            file_csv = csv.reader(f, delimiter=',')
            for row in file_csv:
                result = func(int(row[0]), int(row[1]), int(row[2]))
                rows = f'a = {row[0]}, b = {row[1]}, c = {row[2]}'
                dict_file[str(rows)] = str(result)
        return dict_file
    return wrapper


# Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл
def write_in_json(func):
    def wrapper(file_name, file_name_csv_file, *args, **kwargs):
        with open(file_name + '.json', 'w', encoding='utf=8') as file_json:
            json.dump(func(file_name_csv_file), file_json, indent=4, separators=(',', ':'), ensure_ascii=False)
        print('Запись корней дискриминанта в файл JSON прошла успешно')
    return wrapper
