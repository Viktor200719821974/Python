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
        search_item = str(input('Введіть назву покупки:'))
        listByItem = {}
        print(search_item)
        for key, value in my_list.items():
            if key == search_item:
                value = str(value)
                results = key + " " + value
                print(results)
                value2 = float(value)
                listByItem[value] = listByItem.get(key, 0) + value2
                print(listByItem)
            else:
                print('Такого продукту немає')

    elif choice == '6':
        break
