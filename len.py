# Импортируем модуль tkinter
import tkinter as tk

res = 0

def Convert():#Перевод едениц
    # Получаем значение из текстового поля ввода
    UserInputValue = UserInput.get('1.0', 'end-1c')
    # Если поле ввода пустое, то просто возвращаемся
    if not UserInputValue:
        return
    # Преобразуем введенное значение в число с плавающей точкой
    UserInputValue = float(UserInputValue)
    # С помощью двух переменных определяем единицы измерения, из которых идет перевод и в какие единицы нужно перевести
    if variable.get() == variable2.get():
        return UserInputValue
    elif variable.get() == "Километры" and variable2.get() == "Метры":
        return UserInputValue * 1000
    elif variable.get() == "Километры" and variable2.get() == "Сантиметры":
        return UserInputValue * 100000
    elif variable.get() == "Метры" and variable2.get() == "Километры":
        return UserInputValue / 1000
    elif variable.get() == "Метры" and variable2.get() == "Сантиметры":
        return UserInputValue * 100
    elif variable.get() == "Сантиметры" and variable2.get() == "Километры":
        return UserInputValue / 100000
    elif variable.get() == "Сантиметры" and variable2.get() == "Метры":
        return UserInputValue / 100
    else:
        return None

# Функция для обновления поля с результатом перевода
def UpdateResult(event=None):
    result = Convert()
    # Если результат перевода является целым числом, то преобразуем его в целое число
    if result == int(result):
        result() == int(result)
    # Если результат перевода не является целым числом, то выводим сообщение об ошибке
    else:
        Result.config(text="Invalid input")
    # Получаем результат перевода
    
    # Если результат не получен, то выводим сообщение об ошибке
    if result is None:
        Result.config(text="Invalid input")
    # Иначе выводим результат
    else:
        Result.config(text=f"Result: {result:.2f} {variable2.get()}")

# Функция для обновления единиц измерения при смене типа конвертации
def UpdateType(options):
    # Если выбран тип "Время", то опции меню должны быть соответствующие
    if MainOp.get() == "Time":
        options = ["Seconds", "Minutes", "Hours", "Days"]
    # Если выбран тип "Масса", то опции меню должны быть соответствующие
    elif MainOp.get() == "Mass":
        options = ["Grams", "Kilograms", "Cantners", "Tons"]
    # Иначе опции меню должны быть по умолчанию
    else:
        options = ["Kilometers", "Meters", "Centimeters"]
    # Удаляем старые опции меню
    option_menu2['menu'].delete(0, 'end')
    option_menu1['menu'].delete(0, 'end')
    variable.set(options[0])
    variable2.set(options[0])

def InputCorrettion():
    UserInputValue = UserInput.get('1.0', 'end-1c')



# Создаем графическое окно
window = tk.Tk()
window.geometry('400x300+760+300')
window.title('Converter')

# Создаем надписи и текстовое поле для ввода значения
MainText = tk.Label(window, text='Converter', font='Calibri 28')
UserInput = tk.Text(window, height=1, width=26, wrap='none')
UserInput.bind("<KeyRelease>", UpdateResult)

# Создаем выпадающие списки с единицами измерения
options = ["Kilometers", "Meters", "Centimeters"]
MainOptions = ["Lenght", "Time", "Mass"]

#Создаем Label для вывода результата
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

# создание выпадающего меню для выбора категории конвертации
MM = tk.OptionMenu(window, MainOp, *MainOptions, command=UpdateType) 
# настройка ширины и состояния выпадающего меню
MM.config(width=28, state="normal") 

# создание первого выпадающего меню для выбора единиц измерения
option_menu1 = tk.OptionMenu(window, variable, *options, command=UpdateResult) 
# настройка ширины и состояния первого выпадающего меню
option_menu1.config(width=10, state="normal") 

# создание второго выпадающего меню для выбора единиц измерения
option_menu2 = tk.OptionMenu(window, variable2, *options, command=UpdateResult) 
# настройка ширины и состояния второго выпадающего меню
option_menu2.config(width=10, state="normal") 

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