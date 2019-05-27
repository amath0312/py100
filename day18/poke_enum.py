
from enum import Enum, unique
import random


@unique
class Suite(Enum):
    """花色"""

    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return self.value < other.value
        raise ValueError()


class Card(object):
    suite_char = ['♠️', '♥️', '♣️', '♦️']
    face_char = ['', 'A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        return f'{Card.suite_char[self._suite.value]} {Card.face_char[self._face]}'

    def __repr__(self):
        return str(self)


class Poker(object):

    def __init__(self):
        self._index = 0
        self._cards = [Card(suite, face)
                       for suite in Suite for face in range(1, 14)]

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        card = self._cards[self._index]
        self._index += 1
        return card

    def has_next(self):
        return self._index < len(self._cards)


class Player(object):
    def __init__(self, name):
        self._name = name
        self._cards = []

    @property
    def name(self):
        return self._name

    def get_card(self, card):
        self._cards.append(card)

    def sort(self):
        self._cards.sort(key=lambda card: (card.suite, card.face))

    def show(self):
        for card in self._cards:
            print(card, end='  ')
        print()


def main():
    poker = Poker()
    poker.shuffle()
    players = [
        Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')
    ]
    
    while poker.has_next():
        for p in players:
            if poker.has_next():
                p.get_card(poker.deal())
            else:
                break

    for p in players:
        print(p.name, end=': ')
        p.sort()
        p.show()


if __name__ == '__main__':
    main()
