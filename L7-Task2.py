from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def expenditure(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    @property
    def expenditure(self):
        return f"Расход ткани на {self.name} составит {round(self.size / 6.5 + 0.5, 2)} кв. метра"


class Suit(Clothes):
    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    @property
    def expenditure(self):
        return f"Расход ткани на {self.name} составит {round(2 * self.height + 0.3, 2)} кв. метра"


obj_coat = Coat("пальто 48 размера ", 48)
obj_suit = Suit("костюм 46 размера", 46)
print(obj_coat.expenditure)
print(obj_suit.expenditure)
