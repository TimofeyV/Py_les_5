# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def ApowB(number:int, degree:int):
    if degree == 0:
        return 1
    return number*ApowB(number, degree-1)


number = int(input('Введите число: '))
degree = int(input('Введите степень: '))
print(ApowB(number, degree))