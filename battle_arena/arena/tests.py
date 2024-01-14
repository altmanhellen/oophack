# from django.test import TestCase
from pprint import pprint as pp
import unittest
from arena.utils import (
    Thing,
    Person,
    Paladin,
    Warrior,
)


class TestArena(unittest.TestCase):

    def test_paladin(self):
        ls = []
        for i in range(1, 11):
            ls.append(Paladin(
                f'Перс {i}',
                100 + i,
                13 + i,
                20 + i,
            ))
        print(*ls, sep='\n')
        self.assertEqual(len(ls), 10)

    def test_warrior(self):
        ls = []
        for i in range(1, 11):
            ls.append(Paladin(
                f'Перс {i}',
                100 + i,
                13 + i,
                20 + i,
            ))
        print(*ls, sep='\n')
        self.assertEqual(len(ls), 10)


names = [
    'Андрет', 'Барахир', 'Белемир', 'Беор', 'Берен',
    'Горлим', 'Морвен',  'Риан', 'Дом Халет', 'Авранк',
    'Дорлас', 'Мантор',  'Халет', 'Халмир', 'Харданг',
    'Хунтор', 'Дом Хадора',  'Аэрин', 'Галдор Высокий', 'Марах',
    'Садор Лабадал', 'Хадор',  'Хуор', 'Хурин', 'Брандир',
]

things = [
    'кольчуга', 'мантия', 'посох', 'меч', 'карманный нож',
]

create_caracters(names)