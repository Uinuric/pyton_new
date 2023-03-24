def my_div(arg_1, arg_2):
    return arg_1 / arg_2


var_1 = int(input("Введите числитель "))
var_2 = int(input("Введите знаменатель "))

if var_2 != 0:
    print(f"Результат деления {my_div(var_1, var_2)}")
else:
    print(f"Вы пытаетесь поделить на 0 !!!")
