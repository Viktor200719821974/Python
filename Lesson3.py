# 1.написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
# запишите 5 тудушек
# и выведете все
def notebook():
    todo_list = []
    todo = input()
    print(todo_list)

    def add_todo(*args):
        x = todo_list.append(args)

        def get_all():
            nonlocal x

        get_all()

    add_todo(todo)


print(notebook())

# 2) протипизировать первое задание
# 3) С помощью lambda функции извлеките из списка числа, делимые на 15 без остатка.
# my_list = [45, 56, 67, 776, 5677, 6887, 667, 788, 300]
# f = filter(lambda x: x % 15 == 0, my_list)
# list1 = list(f)
# print(list1)

# 4) написать функцию которая будет принимать целое число n и посчитайте n + nn + nnn.
# Пример:
# summ(7) -> 7+77+777=861
# def sumNumber(n):
#     res = n + n * 11 + n * 111
#     return res
#
#
# print(sumNumber(7))
