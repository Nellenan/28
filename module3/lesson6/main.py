# class Year:
#     def __init__(self, days):
#         self.__days = days
#
#     @property
#     def days(self):
#         return self.__days
#
#     @days.setter
#     def days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise ValueError('Некорректное значение атрибута: {days}')
#
#
# year = Year(365)
# print(year.days)
# year.days = 366
# print(year.days)
# year.days = 367
# print(year.days)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('Вы ещё не родились, пожалуйста покиньте сайт')

        self.__age = age

    @age.deleter
    def age(self):
        print('Год рождения удалён')
        self.__age = None


person = Person('Игорь', 16)
print(person.age)
person.age = 10
print(person.age)

del person.age
print(person.age)