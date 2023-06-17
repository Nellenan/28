# class A:
#     def info(self):
#         print("Это класс А")
#
#
# a = A()
# a.info()
#
#
# class B(A):
#     pass
#
#
# b = B()
# b.info()


class Pet:
    has_tail = True
    legs = 4
    name = None
    animal = None

    def __str__(self):
        result = f"Питомец {self.name}. Это {self.animal}. "\
                 f" У него {'есть хвост' if self.has_tail else 'хвоста нет' }. У него {self.legs} ног(и)."

        return result

    def sound(self):
        pass


class Dog(Pet):
    name = "Чарли"
    animal = "Собака"

    def sound(self):
        return "Гав!"


class Frog(Pet):
    has_tail = False
    name = "Фроппи"
    animal = "Лягушка"

    def sound(self):
        return 'Ква!'


print(Frog())
print(Frog().sound())


# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# vanya = People("vanya", 18)
# dima = People('dima', 17)
#
# print(vanya.name)

