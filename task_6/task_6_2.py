class Road:
    weigth = 25
    tickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        return self._length * self._width * self.weigth * self.tickness / 1000


print(Road(20, 5000).calculate())
