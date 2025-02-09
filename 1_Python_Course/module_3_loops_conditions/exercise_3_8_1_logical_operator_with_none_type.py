a = '' # пустая строка
b = a or 1
print("Вывод значения с использованием логического оператора: ", a, b)
"""
Дело в том, что логические операторы необязательно возвращают булевы значения
(True или False), они возвращают значение одного из операндов. Это происходит согласно следующим правилам:
1. and: если все операнды являются истинными (не нулевые или не пустые), то возвращается последнее 
истинное значение."""
print(1 and "hello" and [False])
# [False]
"""Несмотря на то, что последний операнд похож на False, он является не пустым списком, а значит он истинный.
2. and: если один из операндов является ложным, то такой операнд возвращается первым.
"""
print(42 and 0 and '' and False)
# 0
"""Первый операнд является ненулевым числом — значит истинный, а все остальные (ноль, пустая строка, 
булево значение False) — ложные. И согласно правилу возвращается первый ложный операнд (слева направо).
"""
"""
3. or: если один из операндов является истинным, то такой операнд возвращается первым, а остальные игнорируются.
"""
print([] or 3.14 or False)
# 3.14
"""Первый операнд (пустой список) является ложным, следующий (ненулевое число) — истинным, а значит, 
возвращается именно он, а все остальные игнорируются (не вычисляются).
4. or: если все операнды являются ложными, то возвращается последний.
"""
print(0 or '' or False)
# False
"""Поиск истинного операнда идет также слева направо, но раз ни один такой не нашелся, 
возвращается последнее значение, даже если оно ложное. """
print('*' * 25)
print("Варианты использование оператора None")
a = None
if a is None:
    b = 1
else:
    b = a
print(a, b)
# Выглядит многострочно. Можно использовать тернарный оператор (или его еще называют инлайновым
# условным оператором):

b = a if a is not None else 1
print(b)
# Выглядит гораздо короче, но теперь можно запутаться в большом количестве ключевых слов.
# Согласитесь, что интуитивно очень непонятно. И потому конструкция:

b = a or 1
print(b)

print('*' * 25)
a = "foo"
b = "bar"

print(1 and a or b)

print('*' * 25)
a = ""
b = "bar"

print(1 and a or b)