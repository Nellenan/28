# class User:
#     def __init__(self, hp, method_of_attack, damage, name, species):
#         self.hp = hp
#         self.method_of_attack = method_of_attack
#         self.damage = damage
#         self.name = name
#         self.species = species
#
#     def __str__(self):
#         result = f'Имя {self.name}. Класс {self.species}. Здоровье {self.hp}. Метод атаки {self.method_of_attack}. Урон {self.damage}'
#
#         return result
#
#
# class Warrior(User):
#     def __init__(self, hp, method_of_attack, damage, name):
#         super().__init__(hp * 2, method_of_attack, damage * 1.5, name, 'Воин')
#
#
# class Archer(User):
#     def __init__(self, hp, method_of_attack, damage, name):
#         super().__init__(hp / 2, method_of_attack, damage - 3, name, 'Лучник')
#
#
# class Wizard(User):
#     def __init__(self, hp, method_of_attack, damage, name):
#         super().__init__(hp - 30, method_of_attack, damage - 1, name, 'Маг')
#
#
# warrior = Warrior(100, 'Ближниий бой', 10, "Пепел")
# archer = Archer(100, 'Дальняя атака', 10, 'Робин Гуд')
# wizard = Wizard(100, 'Магическая атака', 10, 'Гарри Потер')
#
#
# print(warrior)
# print(archer)
# print(wizard)
