# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# st = input()
# num_list = []
# num = ''
# for i in st:
#     if i.isdigit():
#         num = num + i + ','
# else:
#     if num != '':
#         num_list.append(num)
#         num = ''
#
# if num != '':
#     num_list.append(num)
# print(num_list)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = input("enter text: ")
# l = len(st)
# list = []
# i = 0
# while i < l:
#     st_int = ''
#     a = st[i]
#     while '0' <= a <= '9':
#         st_int += a
#         i += 1
#         if i < l:
#             a = st[i]
#         else:
#             break
#     i += 1
#     if st_int != '':
#         list.append(int(st_int))
#         print(list)
# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# x = greeting.upper()
# l = list(x)
# print(l)
#
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# l = [pow(i, 2) for i in range(51) if i % 2 == 0]
# print(l)

# function
#
# - створити функцію яка виводить ліст
# def fun_list(list):
#     print(list)

# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def fun_min(a, b, c):
#     return print((a, b, c), 'Min:', min(a, b, c))
#
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def fun_max(a, b, c):
#     return print((a, b, c), 'Max:', max(a, b, c))

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def fun_min_max(*args):
#     return min(args), print('Max:', max(args))

# - створити функцію яка виводить ліст
# def fun_list(list):
# #     print(list)

# - створити функцію яка повертає найбільше число з ліста
# def fun_max_list(list):
#     return print('max:', max(list))
#
#
# l = [46, 667, 788, 97, 7888, 565, 456, 567678]
# fun_max_list(l)


# - створити функцію яка повертає найменьше число з ліста
# def fun_min_list(list):
#     return print('min:', min(list))
#
#
# l = [46, 667, 788, 97, 7888, 565, 456, 567678]
# fun_min_list(l)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def fun_sum_list(list):
#     return print('summa:', sum(list))
#
#
# l = [46, 667, 788, 97, 7888, 565, 456, 567678]
# fun_sum_list(l)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def fun_avg_list(list):
#     return print('avg:', sum(list) / len(list))
#
#
# l = [46, 667, 788, 97, 7888, 565, 456, 567678]
# fun_avg_list(l)
# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
# def decor(function):
#     def wrapper():
#         func = function()
#         make_replace = func.replace('_', ' ')
#         return make_replace
#
#     return wrapper
#
#
# @decor
# def pr():
#     return 'Hello_boss_!!!'
#
#
# print(pr())
