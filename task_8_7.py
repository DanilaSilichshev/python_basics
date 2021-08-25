class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = f"{a}" + "{:+}".format(b) + "i"

    def __str__(self):
        return self.z

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


num_1, num_2 = ComplexNumber(9, -2), ComplexNumber(1, 7)
print(num_1, num_2)
print(num_1 + num_2 * num_1)
