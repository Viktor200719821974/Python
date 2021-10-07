# 1.создать функцию которая будет возвращать сумму разрядов числа в виде строки
#
# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
# def expanded_form(num):
#     result = []
#
#     for index, digit in enumerate(str(num)[::-1]):
#         print(digit)
#         if int(digit) != 0:
#             result.append(digit + ('0' * index))
#
#     return ' + '.join(result[::-1])
#
#
# print(expanded_form(70304))


# 2.создать функцию которая будет выводить сколько и каких символов в строке
# пример:
#
# st = 'as 23 fdfdg544
#
# 'a' -> 1
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
def check_freq(items):
    my_string = {}
    for i in items:
        my_string[i] = items.count(i)
    return my_string


print(check_freq("as 23 fdfdg544"))
