my_list = {'Banyan': 23.4, 'Milk': 20.0, 'Bread': 12.0}
while True:
    print('1. Додати запис про покупку:')
    print('2. Список всіх покупок:')
    print('3. Сума вартості всіх покупок:')
    print('4. Найдорожча покупка:')
    print('5. Пошук по назві покупки:')
    print('6. Вихід:')

    choice = input('Зробіть свій вибір: ')
    if choice not in '123456':
        continue

    elif choice == '1':
        y = str(input('Введіть назву покупки: '))
        x = float(input('Введіть вартість покупки: '))
        my_list.update({y: x})
        print(list)

    elif choice == '2':
        print(my_list)

    elif choice == '3':
        print('Сума витрат:', sum(my_list.values()))

    elif choice == '4':
        print('Найдорожча покупка', max(my_list.values()))

    elif choice == '5':
        a = str(input('Введіть назву покупки:'))
        for i, j in my_list.items():
            if my_list.get(i):
                i = a
                print(i, j)
            else:
                print('Такого продукту немає')

    elif choice == '6':
        break
