with open('my_file_task5.txt', 'w') as f_obj:
    v_num = input("Введите числа через пробел: ")
    f_obj.writelines(v_num)
    my_num = v_num.split()

    print(f" Сумма чисел: {sum(map(int, my_num))}")
