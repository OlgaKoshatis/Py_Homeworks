#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
a = int(input())
b = int(input())
d = int(input())
if (a + b) > d and (a + d) > b and (b + d) > a:
    print(True)
    if a == b == d:
        print('треугольник равносторонний')
    elif a == b or a == d or b == d:
        print('треугольник равнобедренный')
    else:
        print('треугольник разносторонний')
else:
    print(False)