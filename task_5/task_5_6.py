"""Функция, которая из набора символов достает число (если оно единственное и расположено в начале)"""


def get_number_from_string(word):
    number = ""
    for symbol in word:
        if symbol.isdigit():
            number += symbol
    if number != "":
        return float(number)
    else:
        return 0


subjects = dict()
with open('test_6.txt', 'r') as test_file:
    for line in test_file:
        subject, lections, practice, laboratory = line.split()
        subjects[subject] = get_number_from_string(lections) + get_number_from_string(
            practice) + get_number_from_string(laboratory)
print(subjects)
