#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input("Введите количество элементов в массиве: "))
list_A = input("Введите элементы массива через пробел: ").split()
x = int(input("Введите значение X "))
closest = x
diff_list = []
diff = 0
for i in range(n):
    list_A[i] = int(list_A[i])
    diff = abs(x - list_A[i])
    diff_list.append(diff)
    i += 1
tmp = min(diff_list)
index = diff_list.index(tmp)
closest = list_A[index]
print("Самый близкий по величине элемент к заданному 'Х': ", closest)