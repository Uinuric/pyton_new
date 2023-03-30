f_obj = open('my_file_task1.txt', 'w', encoding="utf-8")
while True:
    v_str = input("Введите строку: ")
    f_obj.write(v_str + '\n')
    if not v_str:
        break
f_obj.close()
