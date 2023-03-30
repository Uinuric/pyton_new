with open('my_file_task1.txt', 'r', encoding="utf-8") as f_obj:
    v_line = f_obj.readlines()
    for i in range(len(v_line)):
        v_word = v_line[i].split()
        print(f"Количество слов в строке {i + 1} - {len(v_word)}")
print(f"Количество строк в файле {len(v_line)}")
