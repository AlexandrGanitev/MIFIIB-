"""
Для "распаковки" есть специальный оператор * («звездочка»).

Оператор * чаще всего ассоциируется с операцией умножения, но в Python он имеет и другой смысл.
Этот оператор позволяет «распаковывать» (получить все значения из какой-либо последовательности,
а не саму последовательность) объекты (например, списки или кортежи), внутри которых хранятся
некие элементы. Не используя оператор распаковки, если мы захотим поместить список а в список b,
мы просто укажем его в качестве одного из элементов нового списка. Но если мы захотим добавить
именно значение из первого списка, а не сам список, то как раз оператор распаковки сделает это,
то есть он вытащит из нашего списка все значения.
"""
a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)
# [[1, 2, 3], 4, 5, 6]

a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)
# [1, 2, 3, 4, 5, 6]
# оператор распаковки позволяет работать со значением последовательности,
# а не с самой последовательностью. В первом случае функция print печатает список,
# а во втором — все значения списка:

print(a) # [1, 2, 3]
print(*a)  # 1 2 3
"""
Вернемся к аргументам функций, их существует два вида:

позиционные,  
именованные.
Чтобы функция могла принимать неограниченное количество позиционных аргументов, есть 
специальная конструкция *args, а для именованных аргументов — **kwargs. Аrgs и kwargs не являются 
зарезервированными словами, это просто общее обозначение, args — это сокращение от "arguments" 
(аргументы), а kwargs — сокращение от "keyword arguments" (именованные аргументы). Важно, что они 
должны начинаться с одной и двух звездочек соответственно. Каждая из этих конструкций используется 
для распаковки аргументов соответствующего типа, позволяя вызывать функции со списком аргументов 
переменной длины, как в случае функции print.

Чтобы правильно обрабатывать *args и **kwargs нужно представлять, чем они являются. 
А собственно args — это кортеж, а kwargs  — это словарь."""
def my_func(*args, **kwargs):
   print(type(args))
   print(type(kwargs))

my_func()
# <class 'tuple'>
# <class 'dict'>