"""Заполнение файла числами в пределе от 1 до 1000"""
from random import choice

numbers_list = []
for i in range(100):
    numbers_list.append(str(choice(range(1, 1000))))
file_for_write = open("test_5.txt", "w")
file_for_write.write(" ".join(numbers_list))
file_for_write.close()
"""Подсчёт суммы набора чисел из файла"""
file_for_read = open("test_5.txt", "r")
numbers_sum, numbers_from_file = 0, file_for_read.read().split()
for elem in numbers_from_file:
    numbers_sum += int(elem)
print(f"Сумма чисел в файле: {numbers_sum}")
