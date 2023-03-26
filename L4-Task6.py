'''from itertools import count

my_num = int(input("Введите целое число:"))
for i in count(my_num):
    print(i)
'''
from itertools import cycle

my_list = [1, 2, 3, 4]
for i in cycle(my_list):
    print(i)
