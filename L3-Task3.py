def my_func(arg_1, arg_2, arg_3):
    print(f"Сумма двух наибольших чисел: {arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)}")


my_func(int(input("Число 1:")), int(input("Число 2:")), int(input("Число 3:")))
