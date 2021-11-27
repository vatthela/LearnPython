import random

ENUM_SUIT = {
    1: '♠',
    2: '♣',
    3: '♦',
    4: '♥'
}

ENUM_STATE_INIT = 'INIT'
ENUM_STATE = {
    ENUM_STATE_INIT: 'init'
}


class Card:
    '''Class đại diện cho mỗi lá bài Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')'''
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        '''Hiển thị lá bài'''
        return '{rank}{suit}'.format(suit=self.suit_str(), rank=self.rank)

    def suit_str(self):
        return ENUM_SUIT[self.suit]

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        if self.rank == other.rank:
            return self.suit > other.suit
        return self.rank > other.rank