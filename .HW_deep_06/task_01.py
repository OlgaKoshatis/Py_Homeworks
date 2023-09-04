#Создайте свой модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
k = 8
coord_list = []
answer = ""

for _ in range(k):
p = [int(s) for s in input().split()]

for elem in coord_list:
   if (elem[0] == p[0] or elem[1] == p[1]): #checking for horizontal & vertical crossing
      answer = 'YES'
      break
    elif (elem[0] — p[0] == elem[1] — p[1]) or (elem[0] + elem[1] == p[0] + p[1]):
      answer = 'YES'
      break
     
if answer = 'YES':
    break
else:
    answer = 'NO'
    coord_list.append(p) 
    continue
   
print(answer)