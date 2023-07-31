#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import math

lst1 = [int(i) for i in input().split('/')]
lst2 = [int(i) for i in input().split('/')]

prod1 = lst1[0] * lst2[0]
prod2 = lst1[1] * lst2[1]
num_prod = math.gcd(prod1, prod2)
produce = str(int(prod1/num_prod)) + '/' + str(int(prod2/num_prod))

sum1 = lst1[0] * lst2[1] + lst2[0] * lst1[1]
sum2 = lst1[1] *lst2[1]
num_sum = math.gcd(sum1, sum2)
summa = str(int(sum1/num_sum)) + '/' + str(int(sum2/num_sum))

print(produce, summa, sep='\n')
