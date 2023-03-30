v_trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('my_num.txt', 'r', encoding="utf-8") as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        new_list.append(v_trans[i[0]] + '  ' + i[1])

with open('my_file_task4.txt', 'w', encoding="utf-8") as f_obj2:
    f_obj2.writelines(new_list)
