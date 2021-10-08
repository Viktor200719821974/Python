# Создать класс Rectangle:
# -конструктор принимает две стороны x, y
# -описать арифметические методы:
# + сума площадей двух экземпляров класса
# - разница площадей
# == или площади равны
# != не равны
# >, < меньше или больше
# при вызове метода len() подсчитывать сумму сторон

# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.item = 2 * (x + y)
#
#     def area(self):
#         S = self.x * self.y
#         print('Area :', S)
#         return S
#
#     def __add__(self, other):
#         return self.area() + other.area()
#
#     def __sub__(self, other):
#         return self.area() - other.area()
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __ne__(self, other):
#         return self.area() != other.area()
#
#     def __gt__(self, other):
#         return self.area() > other.area()
#
#     def __lt__(self, other):
#         ordering1 = self.area() < other.area()
#         return print(ordering1)
#
#     def __len__(self):
#         return len(self.item)
#
#
# rectangle1 = Rectangle(2, 3)
# rectangle1.area()
# rectangle2 = Rectangle(6, 7)
# rectangle2.area()
# print(rectangle1.area() < rectangle2.area())

###############################################################################
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта, __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text
l = []


class Letter:
    __count = 0

    def __init__(self, text):
        self.__text = text
        self.__class__.__count += 1

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_value):
        self.__text = new_value

        # text = property(__gettext, __settext)

    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def set_count(cls):
        print('Кількість:', cls.__count)

    def add_text(self, text):
        return print(l.append(self.__text))


letter1 = Letter('должна быть переменная count которая будет')
letter2 = Letter('должна быть переменная count которая будет')
Letter.set_count()
Letter.add_text(letter1, letter2)
###############################################################################
# создать класс Human(name, age) создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденой туфельки, так же должен быть метод который принимает лист золушек и ищет  ту самую
# класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество
# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Prince(Human):
#     def __init__(self, name, age, size_find):
#         super().__init__(name, age)
#         self.size_find = size_find
#
#     def find_size(self):
#         for i in cinderellas:
#             if self.size_find == i.size:
#                 print('Вітаю, ти знайшов свою попелюшку, її звуть:', i.name)
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#         self.__class__.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     @classmethod
#     def set_count(cls):
#         print('Кількість золушок:', cls.count)
#
#
# prince = Prince(name='Ivan', age=20, size_find=34)
# cinderellas = [Cinderella(name='Ola', age=15, size=36),
#                Cinderella(name='Tanya', age=23, size=35),
#                Cinderella(name='Ira', age=22, size=38),
#                Cinderella(name='Lena', age=24, size=39),
#                Cinderella(name='Rita', age=20, size=40),
#                Cinderella(name='Yana', age=18, size=37),
#                Cinderella(name='Masha', age=19, size=34),
#                Cinderella(name='Lesya', age=17, size=35),
#                Cinderella(name='Vera', age=25, size=42),
#                Cinderella(name='Tonya', age=17, size=41)]
# Cinderella.set_count()
# prince.find_size()
