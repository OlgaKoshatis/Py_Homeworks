#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a, b = int(input("Введите число: ")), int(input("Введите степень: "))
def degree(a):
    x = a**b
    return x
print(degree(a))