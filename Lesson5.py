# my_list = {'Banyan': 23.4, 'Milk': 20.0, 'Bread': 12.0}
# while True:
#     print('1. Додати запис про покупку:')
#     print('2. Список всіх покупок:')
#     print('3. Сума вартості всіх покупок:')
#     print('4. Найдорожча покупка:')
#     print('5. Пошук по назві покупки:')
#     print('6. Вихід:')
#
#     choice = input('Зробіть свій вибір: ')
# if choice not in '123456':
#     continue
#
# elif choice == '1':
#     y = str(input('Введіть назву покупки: '))
#     x = float(input('Введіть вартість покупки: '))
#     my_list.update({y: x})
#     print(list)
#
# elif choice == '2':
#     print(my_list)
#
# elif choice == '3':
#     print('Сума витрат:', sum(my_list.values()))
#
# elif choice == '4':
#     print('Найдорожча покупка', max(my_list.values()))
#
# elif choice == '5':
#     search_item = str(input('Введіть назву покупки:'))
#     print(search_item)
#     for key, value in my_list.items():
#         if key == search_item:
#             value = str(value)
#             results = key + " " + value
#             print(results)
#             break
#         # else:
#         #     print('Такого продукту немає')
#
# elif choice == '6':
#     break


class Menu:
    def __init__(self, key, value):
        self.key = str(key)
        self.value = float(value)
        self.fileList = {}

    def add_item(self):
        self.key = input('Введіть назву покупки: ')
        self.value = input('Введіть вартість покупки: ')
        self.fileList.update({self.key: self.value})
        print(list)

    def print_list(self):
        print(self.fileList)

    def sum_item(self):
        print('Сума витрат:', sum(self.fileList.values()))

    def max_value(self):
        print('Найдорожча покупка', max(self.fileList.values()))

        # def value_add(self):
        #     y = str(input('Введіть назву покупки: '))
        #     x = float(input('Введіть вартість покупки: '))
        #     with open('my_list.txt', 'a') as file:
        #         file.write({y}, {x})
        #         print(file)
        # def book_write(self, x):
        #     if x not in '123456':
        #         print('Введіть число від 1-6')
        #     elif x == 1:
        #         self.add_item()
        #     elif x == 2:
        #         self.print_list()
        #     elif x == 3:
        #         self.sum_item()
        #     elif x == 4:
        #         self.max_value()
        #     elif x == 6:
        #         pass


menu1 = Menu('Banana', 23.4)
menu2 = Menu('Milk', 20.0)
menu3 = Menu('Bread', 12.0)

# while True:
#     print('1. Додати запис про покупку:')
#     print('2. Список всіх покупок:')
#     print('3. Сума вартості всіх покупок:')
#     print('4. Найдорожча покупка:')
#     print('5. Пошук по назві покупки:')
#     print('6. Вихід:')
#
#     choice = input('Зробіть свій вибір: ')
#
#     if choice not in '123456':
#         continue
#     elif choice == 1:
#         Menu.add_item()
#     elif choice == 2:
#         Menu.print_list()
#     elif choice == 3:
#         Menu.sum_item()
#     elif choice == 4:
#         Menu.max_value()
#     elif choice == 6:
#         break
Menu.add_item()