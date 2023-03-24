def int_func(v_words):
    return v_words.title()


my_words = (input("Введите слова через пробел: ").split())
res = []
# my_words="kjh hjkjh hjkkjh".split( )
for one_word in my_words:
    res.append(int_func(one_word))
print(res)
