# Напишите небольшую программу, которая реализует ввод
# произвольного количества чисел через пробел и выводит эти же самые числа построчно.

# Пример:
# входные данные:
# 1 2 3 4 5 6 7
# вывод:
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# Примечание для продвинутых программистов:
# попробуйте решить задачу без использования циклов.
numbers = input("Enter your numbers using the Space: ")
# Разбиение строки по разделителю, создаётся список из символов цифр ['1', '2', '3', '4', '5', '6', '7']
numbers_entered = numbers.split()
print(numbers_entered)
# Объединение строк
numbers_joined = '\n'.join(numbers_entered)
print(numbers_joined)