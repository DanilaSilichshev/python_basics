def sum_func():
    total_sum, end = 0, False
    while not end:
        numbers = input('Вводите числа или "В", "в" для прекращения расчёта суммы: ').split()

        current_sum = 0
        for index, element in enumerate(numbers):
            if numbers[index] == 'В' or numbers[index] == 'в':
                end = True
                break
            else:
                current_sum = current_sum + int(numbers[index])
        total_sum = total_sum + current_sum
        print(f'Текущая сумма: {current_sum}')
    print(f'Итоговая сумма: {total_sum}')


sum_func()
