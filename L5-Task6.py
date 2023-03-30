res_line = {}
with open('my_file_task6.txt', 'r', encoding='utf-8') as f_obj:
    v_lines = f_obj.readlines()

for line in v_lines:
    v_data = line.replace('(', ' ').split()
    res_line[v_data[0][:-1]] = sum(int(i) for i in v_data if i.isdigit())
print(res_line)
