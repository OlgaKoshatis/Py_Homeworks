#Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8

import numpy as np

my_list = [int(i) for i in np.random.randint(1, 20, size=10)]
print('Список чисел:', my_list, sep='\n')
counts_list = []
for i in range(len(my_list)):
    count = 1
    next_num = my_list[i] + 1
    for j in range(len(my_list)):
        if next_num in my_list:
            count += 1
            next_num += 1
            j +=1
    counts_list.append(count)
    i += 1
pos = counts_list.index(max(counts_list))
res_list = [my_list[pos], my_list[pos] + max(counts_list) - 1]
print(res_list)