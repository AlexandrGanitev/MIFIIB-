# Задание 3.5.9
# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом
# (читается одинаково слева направо и справа налево).
# Использовать целочисленное деление и деление с остатком не нужно.
# Попробуйте преобразовать число к строке, а потом перевернуть эту строку.
# Смотрите материал прошлого модуля.
num = input("Введите 8-значное число: ")
if len(num) < 8 or len(num)> 8:
    print("Вы ввели не 8-значное число")
list_of_strings = num.split() # список строковых представлений чисел
# print(list_of_strings)
list_of_numbers = list(map(int, list_of_strings)) # список чисел
# print(list_of_numbers)
if num == num[::-1]:
    print(f"Это число {num} - палиндром")
else:
    print(f"Число {num} не палиндром")

print('*' * 25)
num = 12344321
print(str(num) == str(num)[::-1])

