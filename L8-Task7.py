class my_complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        #        return self.a + other.a
        return f"({self.a + other.a}, {self.b + other.b})"

    def __mul__(self, other):
        return f"({self.a * other.a}, {self.b * other.b})"


print(f"Сумма (3, 7) и (2, 5) равна {my_complex(3, 7) + my_complex(2, 5)}")
print(f"Произведение (3, 7) и (2, 5) равна {my_complex(3, 7) * my_complex(2, 5)}")
