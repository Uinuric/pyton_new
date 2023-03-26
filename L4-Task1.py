from sys import argv

script_name, first_param, second_param, third_param = argv

print(f" Заработная плата составила {int(first_param) * int(second_param) + int(third_param)} рублей")
