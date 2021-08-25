class DivisionByZero:
    def __init__(self, *args):
        self.divider = args[0][0]
        self.denominator = args[0][1]

    @staticmethod
    def divide_by_zero(*args):
        try:
            return float(args[0][0]) / float(args[0][1])
        except:
            return DivisionByZero.divide_by_zero(input("Делить на ноль нельзя! Повторите попытку: ").split(" "))


print(DivisionByZero.divide_by_zero(input("Введите 2 числа через пробел: ").split(" ")))
