from itertools import count, cycle

'''' Первая подзадача '''


def nums_generation(start_num, finish_num):
    try:
        for i in count(int(start_num)):
            if i > int(finish_num):
                break
            print(i)
    except ValueError:
        print("Что-то пошло не так! Повторите попытку")
        nums_generation(input("Укажите число начала отсчёта: "), input("Укажите число окончания отсчёта: "))


nums_generation(input("Укажите число начала отсчёта: "), input("Укажите число окончания отсчёта: "))

'''' Вторая подзадача '''
quantity = input("Введите количество элементов списка: ")
test_list, start_point = list(), 0
try:
    while start_point < int(quantity):
        test_list.append(input("Введите элемент списка: "))
        start_point += 1


    def elements_repeat(end_point):
        l = 0
        try:
            for element in cycle(test_list):
                if l >= int(end_point):
                    break
                print(element)
                l += 1
        except ValueError:
            print("Что-то пошло не так! Повторите попытку")
            elements_repeat(input("Укажите точку окончания отсчёта: "))


    elements_repeat(input("Укажите точку окончания отсчёта: "))
except ValueError:
    print("Вы ввели не целое число")
