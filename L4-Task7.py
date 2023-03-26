from math import factorial


def my_func(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)


for el in my_func(int(input("Введите число для извл факториала: "))):
    print(el)
