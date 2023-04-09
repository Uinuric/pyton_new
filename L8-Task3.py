class my_class(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


my_list = []
while True:
    v_num = input("Вводите только числа или Enter:  ")

    if v_num == "":
        break
    try:
        if not v_num.isdigit():
            raise my_class(f"'{v_num}'  не является числом")
        my_list.append(int(v_num))
    except my_class as e:
        print(e)

print(my_list)
