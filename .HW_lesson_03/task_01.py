# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите количество элементов в массиве: "))
list_A = input("Введите элементы массива через пробел: ").split()
x = int(input("Введите искомое число "))

for i in range(n):
    list_A[i] = int(list_A[i])
print("число '",x,"' встречается в заданном массиве", list_A.count(x), " раз(а)")

    