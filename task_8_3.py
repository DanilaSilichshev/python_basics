class ListDataError:
    def __init__(self, empty_list):
        self.num_list = empty_list

    def user_input(self):
        while True:
            try:
                item = int(input("Вводите целые числа и нажимайте Enter: "))
                self.num_list.append(item)
                print(f"Текущий список: {self.num_list}\n")
            except:
                if input("Наберите 'стоп' для выхода или любой символ для продолжения: ") == "стоп":
                    return
                print(f"Недопустимый тип данных - строка")


print(ListDataError([]).user_input())
