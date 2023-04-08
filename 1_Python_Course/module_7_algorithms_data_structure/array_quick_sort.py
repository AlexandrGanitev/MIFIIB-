# Быстрая сортировка так же, как и сортировка слиянием, является одной из самых скоростных. Она также основана на
# принципе «разделяй и властвуй». Однако вместо разделения массивов на части и дальнейшего слияния здесь используется
# другой подход.
#
# Алгоритм выполняется рекурсивно следующим образом:
#
# Выбирается ведущий элемент (есть несколько вариантов, о которых поговорим чуть позже).
# Две части массива сортируются только на основе этого ведущего элемента.
# Происходит последовательный обмен значениями элементов. Вопрос в том, какие элементы обменивать. Сначала
# происходит поиск слева направо до первого элемента, который превосходит по своему значению ведущий элемент.
# Затем массив просматривается справа налево в поисках элемента, который меньше ведущего. Когда такие элементы
# найдены, происходит их обмен.
# Таким образом, в левой части массива имеются элементы только меньше ведущего, а в правой — только больше.
# Функция рекурсивно применяется к получившимся частям массива, если их размеры превосходят один элемент.

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]


def qsort(array, left, right) :
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j :
        while array[i] < p :
            i += 1
        while array[j] > p :
            j -= 1
        if i <= j :
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left :
        qsort(array, left, j)
    if right > i :
        qsort(array, i, right)


qsort(array, 0, len(array) - 1) # наши три аргумента, сам массив, его первый и последний элементы
print(array)
