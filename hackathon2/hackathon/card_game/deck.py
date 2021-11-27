import random
from card import Card

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



class Deck:
    '''Class đại diện cho bộ bài, bao gồm 36 lá'''
    cards = []

    def __init__(self):
        self.state = ENUM_STATE_INIT

    def build(self):
        '''Tạo bộ bài'''
        self.cards = []
        for s in ENUM_SUIT.keys():
            for r in range(1, 10):  # 1 - 9
                self.cards.append(Card(s, r))
        assert len(self.cards) == 36

    def shuffle_card(self):
        '''Trộn bài'''
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        '''Rút một lá bài từ bộ bài'''
        if len(self.cards) == 0:
            raise ValueError('Đã hết card trong bài')
        return self.cards.pop()
