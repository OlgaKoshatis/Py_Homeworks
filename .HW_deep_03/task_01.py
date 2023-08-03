# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов. на входе [1,2,3,1,2,5,6] , на выходе [1,2]

list1 = [i for i in input().split()]
list2 = []
list3 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
    elif list1[i] in list2:
        list3.append(list1[i])

print(*list3)

