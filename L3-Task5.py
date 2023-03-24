def my_func():
    res = 0
    while True:
        v_num = input('Вводите числа через пробел и * для завершения: ').split()
        for i in v_num:
            try:
                if i == '*':
                    print(f'Сумма чисел {res}')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Продолжайте вводить ')
        print(f'Сумма чисел {res}')


my_func()
