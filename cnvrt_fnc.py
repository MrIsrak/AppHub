res = 0

def convert():#Перевод едениц
    global res
    UserInputValue = 0
    name = UserInputValue
    # Если поле ввода пустое, то просто возвращаемся
    if not UserInputValue:
        return
    # Преобразуем введенное значение в число с плавающей точкой
    UserInputValue = float(UserInputValue)
        
    # С помощью двух переменных определяем единицы измерения, из которых идет перевод и в какие единицы нужно перевести
    if variable.get() == variable2.get():
        res =  UserInputValue
    elif variable.get() == "Kilometers" and variable2.get() == "Meters":
        res =  UserInputValue * 1000
    elif variable.get() == "Kilometers" and variable2.get() == "Centimeters":
        res =  UserInputValue * 100000
    elif variable.get() == "Meters" and variable2.get() == "Kilometers":
        res =  UserInputValue / 1000
    elif variable.get() == "Meters" and variable2.get() == "Centimeters":
        res =  UserInputValue * 100
    elif variable.get() == "Centimeters" and variable2.get() == "Kilometers":
        res =  UserInputValue / 100000
    elif variable.get() == "Centimeters" and variable2.get() == "Meters":
        res =  UserInputValue / 100
    ##########
    elif variable.get() == "Seconds" and variable2.get() == "Minutes":
        res = UserInputValue / 60
    elif variable.get() == "Seconds" and variable2.get() == "Hours":
        res = UserInputValue / 3600
    elif variable.get() == "Seconds" and variable2.get() == "Days":
        res = UserInputValue / 86400
    elif variable.get() == "Minutes" and variable2.get() == "Seconds":
        res = UserInputValue * 60
    elif variable.get() == "Minutes" and variable2.get() == "Hours":
        res = UserInputValue / 60
    elif variable.get() == "Minutes" and variable2.get() == "Days":
        res = UserInputValue / 1140
    elif variable.get() == "Hours" and variable2.get() == "Seconds":
        res = UserInputValue * 3600
    elif variable.get() == "Hours" and variable2.get() == "Minutes":
        res = UserInputValue * 60
    elif variable.get() == "Hours" and variable2.get() == "Days":
        res = UserInputValue / 24
    elif variable.get() == "Days" and variable2.get() == "Seconds":
        res = UserInputValue * 86400
    elif variable.get() == "Days" and variable2.get() == "Minutes":
        res = UserInputValue * 1440
    elif variable.get() == "Days" and variable2.get() == "Hours":
        res = UserInputValue * 24
    ##############
    elif variable.get() == "Grams" and variable2.get() == "Kilograms":
        res = UserInputValue / 1000
    elif variable.get() == "Grams" and variable2.get() == "Centners":
        res = UserInputValue / 100000
    elif variable.get() == "Grams" and variable2.get() == "Tons":
        res = UserInputValue / 1000000000
    elif variable.get() == "Kilograms" and variable2.get() == "Grams":
        res = UserInputValue * 1000
    elif variable.get() == "Kilograms" and variable2.get() == "Centners":
        res = UserInputValue / 100
    elif variable.get() == "Kilograms" and variable2.get() == "Tons":
        res = UserInputValue / 1000
    elif variable.get() == "Centners" and variable2.get() == "Grams":
        res = UserInputValue * 100000
    elif variable.get() == "Centners" and variable2.get() == "Kilograms":
        res = UserInputValue * 100
    elif variable.get() == "Centners" and variable2.get() == "Tons":
        res = UserInputValue / 10
    elif variable.get() == "Tons" and variable2.get() == "Grams":
        res = UserInputValue * 1000000
    elif variable.get() == "Tons" and variable2.get() == "Kilograms":
        res = UserInputValue * 1000
    elif variable.get() == "Tons" and variable2.get() == "Centners":
        res = UserInputValue * 100000
    
    else:
        Result.config(text="Invalid input")
        return None
    Result.config(text=f"Result: {res:.2f} {variable2.get()}")
    return res


# Функция для обновления поля с результатом перевода
def update_result(event=None):
    # Получаем результат перевода
    result = convert() 
    # Если результат не получен, то выводим сообщение об ошибке
    if result is None:
        Result.config(text="Invalid input")
    # Иначе выводим результат
    else:
        Result.config(text=f"Result: {result:.2f} {variable2.get()}")

# Функция для обновления единиц измерения при смене типа конвертации
def update_type(options):
    # Если выбран тип "Время", то опции меню должны быть соответствующие
    if MainOp.get() == "Time": 
        options = ["Seconds", "Minutes", "Hours", "Days"]
        update_result()
    # Если выбран тип "Масса", то опции меню должны быть соответствующие
    elif MainOp.get() == "Mass":
        options = ["Grams", "Kilograms", "Cantners", "Tons"]
        update_result()
    # Иначе опции меню должны быть по умолчанию
    else:
        options = ["Kilometers", "Meters", "Centimeters"]
        update_result()
    # Удаляем старые опции меню
    option_menu2['menu'].delete(0, 'end')
    option_menu1['menu'].delete(0, 'end')
    variable.set(options[0])
    variable2.set(options[0])
    for option in options:
        option_menu1['menu'].add_command(label=option, command=lambda value=option: variable.set(value))
        option_menu2['menu'].add_command(label=option, command=lambda value=option: variable2.set(value))

def check_keys(event):
    if event.char.isdigit() == False and not(keyboard.is_pressed('backspace')) and not(keyboard.is_pressed('.')):
        return "break"
