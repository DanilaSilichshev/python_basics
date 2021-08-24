class Cell:
    def __init__(self, quantity):
        # если в качестве количества ячеек передается значение нецелочисленного типа данных,
        # то оно приравнивается к 0
        if isinstance(quantity, int):
            self.quantity = quantity
        else:
            self.quantity = 0

    def __str__(self):
        return f"Количество ячеек в этой клетке равно {self.quantity}"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            return f"Операция вычитания невозможна, значение разности отрицательное"

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row_quantity):
        output = ""
        for row in range(self.quantity // cells_in_row_quantity):
            output += f"{'*'*cells_in_row_quantity}\\n"
        if self.quantity % cells_in_row_quantity != 0:
            output += f"{'*' * (self.quantity % cells_in_row_quantity)}\\n"
        return output


cell_A, cell_B, cell_C, cell_D = Cell(17), Cell(10), Cell(3), Cell("какая-то информация")
print(cell_D)
print(cell_A + cell_B)
print(cell_C - cell_B)
print(cell_B - cell_C)
print(cell_B * cell_C)
print(cell_A / cell_C)
print(cell_B.make_order(3))
