#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

num = input("Введите номер билета ")  
list = [int(i) for i in num]
if len(list) == 6 :
    if sum(list[:3]) == sum(list[3:]) :
        print("Счастливый билет")
    else:
        print("Несчастливый билет") 
else :
    print("Номер билета должен состоять из шести цифр")