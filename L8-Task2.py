class ZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_valid(a, b):
    if b == 0:
        raise ZeroDivision("")
    return a / b


var1 = 15
var2 = 0
try:
    print(f"Результат деления {my_valid(var1, var2)}")
except ZeroDivision as e:
    print(f"Нельзя делить на 0")
