class Clothes:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_coat_expenses(self):
        return self.width / 6.5 + 0.5

    def get_jacket_expenses(self):
        return self.height * 2 + 0.3

    @property
    def get_all_expenses(self):
        return str(f'Общая площадь ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height=0):
        super().__init__(height, width)
        self.coat_expenses = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь, которая затрачивается на пальто {self.coat_expenses}'


class Jacket(Clothes):
    def __init__(self, height, width=0):
        super().__init__(height, width)
        self.jacket_expenses = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь, которая затрачивается на костюм {self.jacket_expenses}'


clothes, coat, jacket = Clothes(20, 4), Coat(7), Jacket(16)
print(clothes.get_all_expenses)
print(coat)
print(jacket)
