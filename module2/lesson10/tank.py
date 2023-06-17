class Tank:
    def __init__(self, hp, armor, damage):
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def shoot(self, enemy):
        enemy.heath_down(self.damage)
        print(f'Есть пробитие  по {enemy}')

    def heath_down(self, damage):
        print(f"По нам попали, урон {damage}")
        total_damage = damage / self.armor
        self.hp -= total_damage


class T34(Tank):
    pass

    def __str__(self):
        return "T34"


class KV44(Tank):
    def __init__(self, hp, armor, damage):
        super().__init__(hp, armor * 10, damage * 100)

    def __str__(self):
        return 'KV44'


t34 = T34(1000, 1500, 200)
kv44 = KV44(1000, 500, 100)

t34.shoot(kv44)
kv44.shoot(t34)