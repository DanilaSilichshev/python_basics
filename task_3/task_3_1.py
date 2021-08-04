def divide_func(dividend, divider):
    try:
        print(int(dividend) / int(divider))
    except ZeroDivisionError:
        print("На 0 делить нельзя! Повторите попытку")
        divide_func(input("Введите делимое: "), input("Введите делитель: "))
    except ValueError:
        print("Вы ввели нечисловое значение или нецелое число! Повторите попытку")
        divide_func(input("Введите делимое: "), input("Введите делитель: "))


divide_func(input("Введите делимое: "), input("Введите делитель: "))
