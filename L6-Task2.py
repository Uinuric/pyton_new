class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def mass_asf(self):
        mass_asf = self._length * self._width * self.weight * self.height / 1000
        print(f"Неободимо {round(mass_asf)} тонн асфальта")


my_class = Road(5000, 20)
my_class.mass_asf()
