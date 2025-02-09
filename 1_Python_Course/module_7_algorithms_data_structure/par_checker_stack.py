def par_checker(string) :
    stack = []  # инициализируем стек

    for s in string :  # читаем строку посимвольно
        if s == "(" :  # если открывающая скобка,
            stack.append(s)  # добавляем её в стек
        elif s == ")" :
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(" :
                stack.pop()  # удаляем из стека
            else :  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0


testing_string = input("Введите пожалуйста вашу строку: \n")
print(par_checker(testing_string))
print(par_checker(str((5 + 6) * (7 + 8) / (4 + 3))))  # в задание не накекалось на конвертирование в строку, добавил
