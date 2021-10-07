# 1.написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
# запишите 5 тудушек
# и выведете все
x1 = '07:00 Прокинутися та приготувати сніданок'
x2 = '08:00 Одягнутися та вийти з дому'
x3 = '09:00 Доїхати до праці'
x4 = '17:00 Закінчити працю та виїхати додому'
x5 = '18:00 Повечеряти, прийняти душ, зайнятися своїми справами, лягти спати'

# def notebook():
#     todo_list = []
#
#     def add_todo(*args):
#         global x1, x2, x3, x4, x5
#         todo_list.append(x1)
#         todo_list.append(x2)
#         todo_list.append(x3)
#         todo_list.append(x4)
#         todo_list.append(x5)
#
#         def get_all():
#             for i in todo_list:
#                 print(i)
#
#         get_all()
#
#     add_todo()
#     return todo_list
#
#
# notebook()

# 2) протипизировать первое задание
from typing import Callable, Union

Value = Union[Callable[[str], None], Callable[[], list[str]]]


def notebook() -> dict[str, Value]:
    todo_list: list[str] = []

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    return {
        "get_all": get_all,
        "add_todo": add_todo
    }


notebook1 = notebook()
notebook1['add_todo']("first")
notebook1['add_todo']("second")
print(notebook1.get('get_all')())

notebook2 = notebook()
notebook2['add_todo']("first2")
notebook2['add_todo']("second2")
print(notebook2.get('get_all')())

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
