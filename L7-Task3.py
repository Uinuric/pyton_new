class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        result = self.quantity - other.quantity
        if result > 0:
            return result
        else:
            return "Операция не выполнена. Разность количества ячеек двух клеток меньше нуля"

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


obj_cell = Cell(12)
obj_cell_add = Cell(14)
print(obj_cell + obj_cell_add)
print(obj_cell - obj_cell_add)
print(obj_cell / obj_cell_add)
print(obj_cell * obj_cell_add)
print(obj_cell.make_order(5))
