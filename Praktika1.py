list = {'Banan': 23.4, 'Milk': 20.0, 'Bread': 12.0}
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
        l = str(input('Введіть назву покупки: '))
        x = float(input('Введіть вартість покупки: '))
        list.update({l: x})
        print(list)

    elif choice == '2':
        print(list)

    elif choice == '3':
        print('Сума витрат:', sum(list.values()))

    elif choice == '4':
        print('Найдорожча покупка', max(list.values()))

    elif choice == '5':
        print()

    elif choice == '6':
        break
