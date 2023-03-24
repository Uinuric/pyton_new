def my_func(arg_1, arg_2):
    return arg_1 ** arg_2


def my_func2(arg_1, arg_2):
    i = 1
    res = arg_1
    while i < arg_2:
        res = res * arg_1
        i += 1
    return res


var_1 = int(input("Введите число: "))
var_2 = int(input("Введите степень: "))
print(f'Результат по варианту 1: {my_func(var_1, var_2)}')
print(f'Результат по варианту 2: {my_func2(var_1, var_2)}')
