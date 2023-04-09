class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        #        return self.a + other.a
        return f"({self.a + other.a}, {self.b + other.b})"

    def __mul__(self, other):
        return f"({self.a * other.a}, {self.b * other.b})"


print(f"Сумма (3, 7) и (2, 5) равна {ComplexNumber(3, 7) + ComplexNumber(2, 5)}")
print(f"Произведение (3, 7) и (2, 5) равна {ComplexNumber(3, 7) * ComplexNumber(2, 5)}")
