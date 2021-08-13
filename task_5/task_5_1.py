with open('test.txt', 'w') as some_file:
    one_line = input('Введите данные для записи в файл: ')
    while True:
        some_file.write(one_line + "\n")
        one_line = input('Введите данные для записи в файл: ')
        if one_line == "":
            break
