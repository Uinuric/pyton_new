class CheckNumbers(Exception):
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
            raise CheckNumbers(f"'{v_num}'  не является числом")
        my_list.append(int(v_num))
    except CheckNumbers as e:
        print(e)

print(my_list)
