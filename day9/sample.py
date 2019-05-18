# -*- coding: utf-8 -*-

import random
import os

class Card(object):

    def __init__(self, suite, face):
        """
        :param suite: 花色
        :param face: 牌点
        """
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face == 1:
            return '%s%s' % (self._suite, 'A')
        elif self._face == 11:
            return '%s%s' % (self._suite, 'J')
        elif self._face == 12:
            return '%s%s' % (self._suite, 'Q')
        elif self._face == 13:
            return '%s%s' % (self._suite, 'K')
        else:
            return '%s%s' % (self._suite, self._face)

class Poker(object):

    def __init__(self):
        self._cards = [
                Card(suite, face)
                for suite in '♠♥♣♦'
                for face in range(1,14)
            ]    

    @property
    def cards(self):
        return tuple(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)
    
    def deal(self, group):
        """发牌
        :param group: 将扑克牌分成group组
        :return: group组牌
        """
        index = 0
        dealed_cards = []
        for _ in range(group):
            dealed_cards.append([])

        for card in self._cards:
            dealed_cards[index].append(card)
            index += 1
            index = index % group
        return dealed_cards

    def display(self):
        Poker.display_cards(self._cards)
    
    @staticmethod
    def display_cards(cards):
        for card in cards:
            print(card, end=' ')
        print()

    @staticmethod
    def arrange(cards, key):
        return sorted(cards, key=key)


if __name__ == '__main__':
    poker = Poker()
    poker.shuffle()
    poker.display()
    dealed = poker.deal(4)
    for player_cards in dealed:
        sorted_cards = Poker.arrange(player_cards, key=lambda card: (card.suite, card.face))
        Poker.display_cards(player_cards)
        Poker.display_cards(sorted_cards)

    