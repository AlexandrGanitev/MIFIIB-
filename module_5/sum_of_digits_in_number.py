"""Задание 5.2.5
Задание на самопроверку.

Дано натуральное число N. Вычислите сумму его цифр.

При решении этой задачи нельзя использовать строки, списки,
массивы (ну и циклы, разумеется)."""


def sum_digit(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digit(n // 10)


my_number = int(input("Введите натуральное число: \n"))
print(sum_digit(my_number))