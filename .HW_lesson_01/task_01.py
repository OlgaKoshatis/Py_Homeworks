#Найдите сумму цифр трехзначного числа.

n = int(input())
dig_sum = 0
while n > 0 :
    dig = n % 10
    dig_sum += dig
    n //= 10
print(dig_sum)