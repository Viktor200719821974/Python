# 1)Дан лист:
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# - найти min число в листе
# list.sort()
# print(list[0])

# - удалить все дубликаты в листе
# del list[5]
# del list[6]
# del list[7]
# print(list)
# list.remove(5)
# list.remove(2)
# list.remove(8)
# print(list)


# - заменить каждое четвертое значение на "Х"
# del list[3]
# list.insert(3, 'x')
# del list[7]
# list.insert(7, 'x')
# print(list)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# a = 15
# print('*', a * '*', '*')
# print('*',  a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * ' ', '*')
# print('*', a * '*', '*')

# 3) вывести табличку умножения с помощью цикла while
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i * j, end=' ')
#         j = j + 1
#     print()
#     i = i + 1

# 4) переделать первое задание под меню с помощью цикла
# x = int(input('Зробіть свій вибір(1-6):'))
# if x == 1:
#     print('1. найти min число в листе')
# elif x == 2:
#     print('2.удалить все дубликаты в листе')
# elif x == 3:
#     print('3.заменить каждое четвертое значение на "Х"')
# elif x == 4:
#     print('4.вывести на экран пустой квадрат из "*" сторона которого указана в переменой')
# elif x == 5:
#     print('5.вывести табличку умножения с помощью цикла while')
# elif x == 6:
#     print('6.Вихід')
# else :
#     print('Зробіть інший вибір')
# l = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 2, 7, 9]
# while True:
#     print('1. найти min число в листе')
#     print('2. удалить все одинаковые значения')
#     print('3. заменить каждое четвертое значение на "Х"')
#     print('4. вывести элемент листа, значение которого ближе всего к среднему арифметическому всех елементов в листе')
#     print('5. выход')
#
#     choice = input('Сделайте свой выбор: ')
#     if choice not in '123456':
#         continue
#
#     elif choice == '1':
#         min_num = l[0]
#         for item in l:
#             if min_num > item:
#                 min_num = item
#         print(l)
#         print('min_num: ', min_num)
#
#     elif choice == '2':
#         l2 = l.copy()
#         for i in range(len(l2) - 1, -1, -1):
#             if l2.count(l2[i]) > 1:
#                 del l2[i]
#
#         print(l)
#         print(l2)
#
#     elif choice == '3':
#         l2 = l.copy()
#         for i in range(3, len(l2), 4):
#             l2[i] = 'X'
#         print(l2)
#
#     elif choice == '4':
#         print('List =', l)
#         l.sort()
#         sum = 0
#         for i in l:
#             sum += i
#         avg = sum / len(l)
#
#         candidates = []
#
#         for i in range(len(l)):
#             if l[i] > avg:
#                 candidates.append(l[i])
#                 candidates.append(l[i - 1])
#                 break
#         print("Avg =", avg)
#
#         if not len(candidates):
#             print('result:', avg)
#         else:
#             print('result = ', candidates[0] if avg > (candidates[0] + candidates[1]) / 2 else candidates[1])
#
#     elif choice == '5':
#         break
#
# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

# list.sort()
# b = sum(list)/len(list)
# for i in list:
#     if list[i] <= b:
#        print(list[i])
#     else:
#

