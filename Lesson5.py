# while True:
#     print('1. Додати запис про покупку:')
#     print('2. Список всіх покупок:')
#     print('3. Сума вартості всіх покупок:')
#     print('4. Найдорожча покупка:')
#     print('5. Пошук по назві покупки:')
#     print('6. Вихід:')
#
#
#     class Menu:
#         def __init__(self, a, b):
#             self.a = a
#             self.b = b
#             self.fileList = {}
#
#         def add_item(self):
#             # key = input('Введіть назву покупки: ')
#             # value = input('Введіть вартість покупки: ')
#             res = dict(zip(self.a, self.b))
#             with open('list.txt', 'a') as file:
#                 file.write(res)
#
#
#     #
#     #     def print_list(self):
#     #         print(self.fileList)
#     #
#     #
#     #     def sum_item(self):
#     #         print('Сума витрат:', sum(self.fileList.values()))
#     #
#     #
#     #     def max_value(self):
#     #         print('Найдорожча покупка', max(self.fileList.values()))
#     #
#     #
#     #     def book_write(self, x):
#     #         if x not in '123456':
#     #             print('Введіть число від 1-6')
#     #         elif x == 1:
#     #             self.add_item()
#     #         elif x == 2:
#     #             self.print_list()
#     #         elif x == 3:
#     #             self.sum_item()
#     #         elif x == 4:
#     #             self.max_value()
#     #         elif x == 6:
#     #             pass
#     #
#     #
#     #      menu1 = Menu('Banana', 23.4)
#     #      menu2 = Menu('Milk', 20.0
#
#     # Menu.book_write(choice)
#     # Menu.add_item()
#
#     # def add_item1():
#     #     key = input('Введіть назву покупки: ')
#     #     value = input('Введіть вартість покупки: ')
#     #     res = {}
#     #     res = dict(zip(key, value))
#     #     with open('list.txt', 'a') as file:
#     #         file.write(res)
#     #
#     #     add_item1()
#     choice = input('Зробіть свій вибір: ')
#     if choice not in '123456':
#         continue
#     elif choice == 1:
#         key = str(input('Введіть назву покупки: '))
#         value = float(input('Введіть вартість покупки: '))
#         Menu.add_item(key, value)
#     elif choice == 6:
#         break
#     # else:
#     #     print('Введіть число від 1-6')

a = str(input())
b = float(input())
res = {}
res[a] = b
with open('items.txt', 'w') as file:
    file.write(repr(res))
