def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x > 0 and y < 0:
            # print(x ** y)
            current_degree, result = 1, 1
            while abs(y) >= current_degree:
                result *= x
                current_degree += 1
            result = 1/result
            print(result)
        else:
            print("Вы ввели число, которое не входит в указанный диапазон! Повторите попытку")
            my_func(input("Введите действительное положительное число: "), input("Введите целое отрицательное число: "))
    except ValueError:
        print("Вы ввели нечисловое значение или число неверного типа! Повторите попытку")
        my_func(input("Введите действительное положительное число: "), input("Введите целое отрицательное число: "))


my_func(input("Введите действительное положительное число: "), input("Введите целое отрицательное число: "))
