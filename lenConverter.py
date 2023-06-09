# Импортируем модуль tkinter и keyboard
import tkinter as tk
import keyboard
from cnvrt_fnc import *
res = 0

def convert():#Перевод едениц
    global res
    # Получаем значение из текстового поля ввода
    UserInputValue = UserInput.get('1.0', 'end-1c')
    UV = UserInput.get('1.0', 'end-1c')
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

# Создаем графическое окно
window = tk.Tk()
window.geometry('400x300+760+300')
window.title('Converter')

# Создаем надписи и текстовое поле для ввода значения
MainText = tk.Label(window, text='Converter', font='Calibri 28')
UserInput = tk.Text(window, height=1, width=26, wrap='none')
if keyboard.is_pressed('enter'):
    update_result()

UserInput.bind("<Key>", check_keys)
UserInput.bind("<KeyRelease>", update_result)

# Создаем выпадающие списки с единицами измерения
options = ["Kilometers", "Meters", "Centimeters"]
MainOptions = ["Lenght", "Time", "Mass"]

Result = tk.Label(window, text='Result: ' + str(res), font='Calibri 14', wraplength=400)


# создание строковой переменной для первого выпадающего меню
variable = tk.StringVar(window) 
# создание строковой переменной для второго выпадающего меню
variable2 = tk.StringVar(window)
# создание строковой переменной для главного выпадающего меню
MainOp = tk.StringVar(window) 

# создание выпадающего меню
# установка начального значения для первого выпадающего меню
variable.set(options[0]) 
# установка начального значения для второго выпадающего меню
variable2.set(options[0]) 
# установка начального значения для главного выпадающего меню
MainOp.set(MainOptions[0]) 

# создание первого выпадающего меню для выбора единиц измерения
option_menu1 = tk.OptionMenu(window, variable, *options, command=update_result) 
# настройка ширины и состояния первого выпадающего меню
option_menu1.config(width=10, state="normal") 

# создание второго выпадающего меню для выбора единиц измерения
option_menu2 = tk.OptionMenu(window, variable2, *options, command=update_result) 
# настройка ширины и состояния второго выпадающего меню
option_menu2.config(width=10, state="normal") 

# создание выпадающего меню для выбора категории конвертации
MM = tk.OptionMenu(window, MainOp, *MainOptions, command=update_type)
#print(UpdateType(options))

# настройка ширины и состояния выпадающего меню
MM.config(width=28, state="normal") 



# размещение заголовка окна в определенном месте
MainText.place(x=125, y=15) 
# размещение поля ввода пользовательских данных в определенном месте
UserInput.place(x=90, y=120) 
# размещение выпадающего меню выбора категории конвертации в определенном месте
MM.place(x=90, y=148) 
# размещение результата конвертации в определенном месте
Result.place(x=88, y=220) 
# размещение первого выпадающего меню выбора единиц измерения в определенном месте
option_menu1.place(x=88, y=180) 
# размещение второго выпадающего меню выбора единиц измерения в определенном месте
option_menu2.place(x=198, y=180) 
# запуск основного цикла обработки событий окна (ожидание пользовательского ввода)
window.mainloop()