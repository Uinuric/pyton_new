from functools import reduce

# my_list = [i for i in range(1, 11, 2)]
my_list = [i for i in range(100, 1001, 2)]
new_list = reduce(lambda x, y: x * y, my_list)
print(new_list)
