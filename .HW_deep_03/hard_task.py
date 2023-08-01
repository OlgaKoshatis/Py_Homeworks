# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 10) многочлена и записать как многочлен степени k.


import random
import sympy
import math
 

k = int(input('Введите натуральную степень k:\t'))

coefficient_list=[random.randint(0, 11) for i in range(k+1)]
x = sympy.symbols('x')
x_pows_list = [x**i for i in range(k+1)]

print (sum(map(math.prod,zip(coefficient_list, x_pows_list))), '= 0')