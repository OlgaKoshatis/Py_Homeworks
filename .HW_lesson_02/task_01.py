#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
n = int(input("Введите количество монет "))
count_avers = 0
count_revers = 0
print("avers - введите 1, revers - введите 2")
for i in range(n) :
    x = int(input())
    if x == 1 :
        count_avers += 1
    elif x == 2 :
        count_revers += 1
    else :
        print("не считается")
        break
    i += 1
if count_avers <= count_revers :
    print("минимальное количество монет, которое нужно перевернуть -", count_avers)
else :
    print("минимальное количество монет, которое нужно перевернуть -", count_revers)