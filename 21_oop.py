import importlib
from random import shuffle


cards = importlib.import_module('cards').cards
shuffle(cards)

class Gamer:

    def __init__(self, name):
        self.point = 0
        self.hand = []
        self.end = False
        self.name = name

    def check(point):
        return point <= 21

    def next(self):
        card = cards.pop()
        self.hand.append(card[0])
        self.point += card[1]

        print(card[0])
    
    def end(self):
        self.end = True


class Computer(Gamer):

    def check_points(func):
        def wrapper(self):
            if self.point <= 19:
                func(self)
            else:
                self.end = True
        return wrapper

    @check_points
    def next(self):
        Gamer.next(self)


comp = Computer('Компьютер')

comp.next()
print(comp.point)
print(comp.end)
comp.next()
print(comp.point)
print(comp.end)
comp.next()
print(comp.point)
print(comp.end)
comp.next()
print(comp.point)
print(comp.end)
comp.next()
print(comp.point)
print(comp.end)