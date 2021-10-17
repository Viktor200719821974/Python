import json


class NoteBook:
    def __init__(self, filelist:str):
            self.__fileList = f'{filelist}.json'

    def __parse_file(self) -> list[dict]:
            try:
                with open(self.__fileList) as file:
                    return json.load(file)
            except:
                return []

    def __save(self, data: list[dict]):
        with open(self.__fileList, 'w') as file:
                json.dump(data, file)

    def add_item(self):
            key = input('Введіть назву покупки: ')
            value = input('Введіть вартість покупки: ')
            if not value.isdigit():
                print('input ERROR')
            key = self.__parse_file()
            print(key)
            key.append(dict(key = key, value=float(value)))
            self.__save(key)

    def print_list(self):
        key = self.__parse_file()
        if not key:
            print('NOT FOUND')
        for i in key:
            print(i)


    def sum_value(self):
            print('Сума витрат:', sum([i['value'] for i in self.__parse_file()]))


    def max_value(self):
            print('Найдорожча покупка', max([i['value'] for i in self.__parse_file()]))


    def search_key(self):
        key = input('Введіть назву покупки:')
        for i in self.__parse_file():
           if i ['key'] == key:
            print(i)
            break
        print('NOT FOUND')

noteBook = NoteBook('my_notebook')

while True:
    print('1. Додати запис про покупку.')
    print('2. Список всіх покупок.')
    print('3. Сума вартості всіх покупок.')
    print('4. Найдорожча покупка.')
    print('5. Пошук по назві покупки.')
    print('6. Вихід.')

    choice = input('Зробіть свій вибір: ')

    if choice not in ['1','2','3','4','5','6']:
        continue

    elif choice == '1':
        noteBook.add_item()
    elif choice == '2':
        noteBook.print_list()
    elif choice == '3':
        noteBook.sum_value()
    elif choice == '4':
        noteBook.max_value()
    elif choice == '5':
        noteBook.search_key()
    elif choice == '6':
        break


