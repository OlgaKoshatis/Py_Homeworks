#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.Пользователь вводит 2 числа: n — кол-во элементов первого множества, m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
n, m = int(input("Количество элементов первого множества: ")), int(input("Количество элементов второго множества: "))
arr_n = [int(i) for i in input("Элементы первого множества: ").split()]
arr_m = [int(i) for i in input("Элементы второго множества: ").split()]
arr_nm = []
for j in set(arr_n):
    for k in set(arr_m):
        if k == j:
            arr_nm.append(k)
        else:
            continue
arr_nm.sort()
print(*arr_nm)