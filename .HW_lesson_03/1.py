list_1 = [1, 2, 3, 4, 5]
k = int(input('k = '))

k = k % len(list_1)
list_res = []
for i in range(k):
    list_res.append(list_1[len(list_1) - k + i])
print(list_res)
