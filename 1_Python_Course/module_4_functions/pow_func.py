# функция, которая возводит любое число в квадрат
def pow_func(base):
   print(base ** 2)

pow_func(3)  # 9
pow_func(5)  # 25

# Если попытаться вызвать эту функцию без передачи ей аргументов, то вы получите следующую ошибку:

# pow_func()
# TypeError: pow_func() missing 1 required positional argument: 'base'
print('*' * 25, 'Вариант 2')
# Пусть наша функция теперь возводит число в любую степень, но по умолчанию возводит в степень 2.
# Тогда её объявление будет выглядеть следующим образом:

# функция, которая возводит любое число в степень n
def pow_func(base, n=2):
   print(base ** n)

pow_func(3)  # 9
pow_func(5, 3)  # 125