# объявили функцию для подсчета количества символов в неком абстрактном тексте
def char_frequency(text) :
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", "")

    count = {}  # для подсчета символов и их количества
    for char in text :
        if char in count :  # если символ уже встречался, то увеличиваем его количество на 1
            count[char] += 1
        else :
            count[char] = 1

    for char, cnt in count.items() :
        print(f"Символ {char} встречается {cnt} раз")
