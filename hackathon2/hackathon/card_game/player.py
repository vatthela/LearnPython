class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self,name):  # dễ
        self.name = name
        self.cards = []

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        point = 0
        for card in self.cards:
            point += card.rank
        return point

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        return max(self.cards)

    def add_card(self,card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        if len(self.cards) == 3:
            raise ValueError('Người chơi đã rút đủ bài')
        self.cards.append(card)

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.cards = []
        
    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        return "{player} {cards} Điểm:{point} | Lá bài lớn nhất:{biggest_card}".format(
            **{'player': self.name,
               'cards': " ".join([str(card) for card in self.cards]),
               'point': self.point,
               'biggest_card': self.biggest_card})