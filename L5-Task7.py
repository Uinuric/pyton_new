import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('my_file_task7.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('my_file_task7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
