# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
# (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом
# проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    total_textile = 0

    @abstractmethod
    def textile_clothes(self):
        pass

    def __add__(self, other):
        Clothes.total_textile = self.textile_clothes + other.textile_clothes
        return Clothes.total_textile


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def textile_clothes(self):
        v = round((self.v / 6.5 + 0.5), 2)
        return v


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def textile_clothes(self):
        h = round((2 * self.h + 0.3), 2)
        return h


coat = Coat(5)
coat2 = Coat(7)
print(coat.textile_clothes)
print(coat2.textile_clothes)

suit = Suit(5)
suit2 = Suit(7)
print(suit.textile_clothes)
print(suit2.textile_clothes)

print(coat + suit)
print(coat2 + suit2)
# print(coat + suit + coat2 + suit2)
