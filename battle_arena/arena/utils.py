import random
from pprint import pprint as pp


class Thing:
    def __init__(self, name, protection, attack, life):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.life = life

    def __str__(self):
        return f'{self.name} {self.protection} {self.attack} {self.life}'

    def __repr__(self):
        return f'{self.name} {self.protection} {self.attack} {self.life}'


class Person:
    def __init__(self, name, hp, base_attack, base_protection):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_protection = base_protection
        self.things = set()

    def set_things(self, thing):
        self.things.add(thing)

    def calculate_total_protection(self):
        total_protection = self.base_protection
        for thing in self.things:
            total_protection += thing.protection
        return total_protection

    def receive_damage(self, attack_damage):
        final_protection = self.calculate_total_protection()
        damage = attack_damage - attack_damage * final_protection
        self.hp -= damage
        return damage


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp * 2, base_attack, base_protection * 2)

    def __str__(self):
        return f'Паладин: {self.name} {self.hp} {self.base_attack} {self.base_protection}'


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack * 2, base_protection)

    def __str__(self):
        return f'Воин: {self.name} {self.hp} {self.base_attack} {self.base_protection}'


THINGS = [
    'кольчуга', 'мантия', 'посох', 'меч', 'карманный нож',
    'телефон', 'волшебная книга', 'порох', 'гатлинг', 'винтовка',
    'базука', 'волшебная подкова', 'копьё', 'лук и стрелы', 'титановая броня',
]

NAMES = [
    'Андрет', 'Барахир', 'Белемир', 'Беор', 'Берен',
    'Горлим', 'Морвен',  'Риан', 'Дом Халет', 'Авранк',
    'Дорлас', 'Мантор',  'Халет', 'Халмир', 'Харданг',
    'Хунтор', 'Дом Хадора',  'Аэрин', 'Галдор Высокий', 'Марах',
    'Садор Лабадал', 'Хадор',  'Хуор', 'Хурин', 'Брандир',
]


class CreatePers:

    def __init__(self):
        self.things = self.create_things()
        self.caracters = self.create_caracters()
        self.assign_things()

    def create_things(self):
        things = []
        for _ in range(len(THINGS)):
            name = random.choice(THINGS)
            protection = random.uniform(0, 0.1)
            attack = random.randint(1, 10)
            life = random.randint(1, 10)
            things.append(Thing(name, protection, attack, life))
        things.sort(key=lambda x: x.protection)
        return things

    def create_caracters(self):
        caracters = []
        for _ in range(10):
            name = NAMES.pop()
            hp = random.randrange(100, 200)
            base_attack = random.randrange(10, 20)
            base_protection = random.uniform(0, 0.1)  # 0.1
            class_choice = random.choice([Paladin, Warrior])
            caracters.append(class_choice(
                name, hp, base_attack, base_protection,))
        return caracters

    def assign_things(self):
        for war in self.caracters:
            for _ in range(1, random.randrange(2, 5)):
                war.set_things(random.choice(self.things))


def battle_arena(caracters):

    while len(caracters) > 1:
        attacker, defender = random.sample(caracters, 2)
        damage = defender.receive_damage(attacker.base_attack)
        print(f'{attacker.name} наносит удар по {defender.name} на {damage} урона')

        if defender.hp <= 0:
            print(f'{defender.name} был убит!')
            caracters.remove(defender)

    print(
        f'Бой между {attacker.name} и {defender.name} окончен. Победитель битвы: {caracters[0].name}')


def perform_attack(attacker, defender, caracters):
    """Функция симулирует удар"""
    attacker, defender = random.sample(caracters, 2)
    damage = defender.receive_damage(attacker.base_attack)
    print(f"{attacker.name} атакует {defender.name}, причиненный урон: {damage:.2f}.")
    print(f"У {defender.name} осталось {defender.hp:.2f} HP.\n")


persons = CreatePers()
attacker = persons.caracters[0]
defender = persons.caracters[1]
for pers in (attacker, defender, ):
    print('-' * 30, pers.name, '-' * 30)
    print(f'Имя: {pers.name}')
    print(f'Здоровье: {pers.hp}')
    print(f'Базовая атака: {pers.base_attack}')
    print(f'Базовая защита: {pers.base_protection}')
    print()
    for i, t in enumerate(pers.things, start=1):
        print('-'*5, f'Вещь {pers.name} № {i}', '-'*5)
        print(f'Вещь: {t.name}')
        print(f'Защита: {t.protection}')
        print(f'Атака: {t.attack}')
        print(f'Жизнь: {t.life}')


perform_attack(attacker, defender, persons.caracters)
