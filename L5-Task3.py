with open('my_firm.txt', 'r', encoding="utf-8") as f_obj:
    v_salary = []
    v_salary20 = []
    my_list = f_obj.read().split('\n')
    for i in my_list:
        i = i.split()
        print(i)
        if int(i[1]) < 20000:
            v_salary20.append(i[0])
        v_salary.append(i[1])
print(f"Сотрудники с окладом меньше 20 т.р. {v_salary20}")
print(f"Cредний оклад {sum(map(int, v_salary)) / len(v_salary)}")
'''
Иванов 15000
Петров 10000
Сидоров 25000
Козлов 30000
Курочкин 5000
Петухов 35000
Быков 12000
Конев 10000
Кошкин 40000
Баранов 50000'''
