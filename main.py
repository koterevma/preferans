#!/usr/bin/env python3
from enum import Enum, auto
from itertools import chain, repeat
from random import shuffle
from collections import Counter


PLAYERS_COUNT = 3
EMULATE_COUNT = 1_000_000

class Card(Enum):
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    J = auto()
    Q = auto()
    K = auto()
    A = auto()


def create_deck() -> list[Card]:
    return list(chain.from_iterable([repeat(card, 4) for card in list(Card)]))


def emulate_selection():
    deck = create_deck()
    shuffle(deck)
    player_selected = 0
    while deck.pop() != Card.SIX:
        player_selected = (player_selected + 1) % PLAYERS_COUNT

    return player_selected


def main():
    players_selected = list()
    for _ in range(EMULATE_COUNT):
        players_selected.append(emulate_selection())

    counter = Counter(players_selected)
    for player, count in counter.items():
        print("Player %d selected %d times. Probability is %.3f" % (player, count, count / EMULATE_COUNT))


if __name__ == '__main__':
    main()
