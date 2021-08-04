int_func = lambda word: word.capitalize()
str_data = input("Введите строку, состоящую из слов с латинскими буквами в нижнем регистре: ")
str_data = str_data.split(" ")
for index, element in enumerate(str_data):
    str_data[index] = int_func(element)
print(" ".join(str_data))
