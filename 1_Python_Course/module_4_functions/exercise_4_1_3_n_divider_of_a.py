"""
Задание 4.1.3
Задание на самопроверку.

Напишите функцию, которая проверяет, является ли число n делителем числа a. И выводит на экран
соответствующее сообщение, является ли число делителем или нет.
"""
def check_divider_func(a, n):
    if a % n == 0:
        print(f"Число {n} является делителем числа {a} ")
        return True
    else:
        print(f"Число {n} не является делителем числа {a} ")
        return False

a = int(input("Введите делимое: "))
n = int(input("Введите делитель: "))
print(check_divider_func(a, n))
print('*' * 25, "Вариант 2")
def check_num(a, n):
   if a % n == 0:
       print(f"Число {n} является делителем числа {a}")
   else:
       print(f"Число {n} не является делителем числа {a}")

check_num(4, 2)  # Число 2 является делителем числа 4
check_num(5, 2)  # Число 2 не является делителем числа 5
