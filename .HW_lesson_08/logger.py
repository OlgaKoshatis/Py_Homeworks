from data_create import input_user_data


def input_data():
    name, surname, phone, address = input_user_data()
    var = int(input(f'\nВ каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{address}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{address}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{address}\n\n')
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')
    


    
def print_data():
    var = int(input('Какой файл показать:\n'
                    f' - 1 \n'
                    f' - 2 \n'
                    f'Ваш выбор: \n\n'))
    
    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_1st = list(file.readlines())
            j = 0
            data_1_1st = []
            for i in range(len(data_1st)):
                if data_1st[i] == '\n':
                    data_1_1st.append(''.join(data_1st[j:i]))
                    j = i
            print(''.join(data_1_1st))

    if var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_2nd = list(file.readlines())
            print(''.join(data_2nd))


def change_data() -> None:

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    
    data_to_edit = input('Введите данные для поиска: ')
    data_to_edit = search(data, data_to_edit)
    print(f'Выбранный контакт: {data_to_edit}')

    var = int(input(f'Удалить или изменить?'
                    f' - 1 \n'
                    f' - 2 \n'
                    f'Ваш выбор: \n\n'))
    if var == 1:
        data.remove(data_to_edit)
    elif var == 2:
        data[data.index(data_to_edit)] = enter_contact(data_to_edit)

    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))
