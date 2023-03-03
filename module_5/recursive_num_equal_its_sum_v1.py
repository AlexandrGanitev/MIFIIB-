"""
Задание 5.5.11
Задание на самопроверку.
Поработаем над более сложной рекурсивной функцией. Сейчас попробуем реализовать функцию equal(N, S),
проверяющую, совпадает ли сумма цифр числа N с числом S. При написании программы следует обратить
внимание на то, что, если S стала отрицательной, то необходимо сразу вернуть False.
Реализуйте описанную выше функцию."""


def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10) # очень лаконично!


my_number = int(input("Введите натуральное число состоящее из n цифр: \n"))
number_s = int(input("Введите некое число S: \n"))
print("Равны ли сумма цифр числа N и число S? \n")
if equal(my_number, number_s):
    print("Равны")
else:
    print("Не равны")