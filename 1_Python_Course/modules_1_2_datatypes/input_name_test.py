first_name = input("Введите ваше имя:")
last_name = input("Введите вашу фамилию:")
age = input("Введите ваш возраст:")
city = input("Введите город проживания:")

# Выводим пустую строку
print("")

# Выводим приветствие, подставляя имя и фамилию пользователя,
# которые он ввел с клавиатуры
print("Привет,", first_name, last_name + "!")

# Выводим пустую строку
print("")

# Выводим фиксированный текст для удобства просмотра
print("Ваш профиль:")

# Выводим возраст и город, которые указал пользователь
print("Возраст:", age, "лет")
print("Город:", city)