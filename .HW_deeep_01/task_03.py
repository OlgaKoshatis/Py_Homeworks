#Посчитать сумму цифр любого целого или вещественного числа, которое введет пользователь. Через строку решать нельзя. Можно юзать decimal.

num = (input())

from decimal import Decimal

num = Decimal(num)
digits = num.as_tuple().digits
print(sum(digits))