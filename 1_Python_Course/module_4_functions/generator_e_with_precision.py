"""
Теперь попробуем написать генератор для приближенного вычисления числа e = 2.718.
Для нахождения числа, удовлетворяющего необходимой точности будем использовать следующий цикл:
"""


def e():
    n = 1

    while True:
        yield (1 + 1 / n) ** n
        n += 1


last = 0
for a in e():  # e() - генератор
    if (a - last) < 0.00000001:  # ограничение на точность
        print(a)
        break  # после достижения которого - завершаем цикл
    else:
        last = a  # иначе - присваиваем новое значение


print('*' * 25, "Итерируем вручную:")
iter_obj = iter("Hello!")

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

