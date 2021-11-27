
from deck import Deck
from player import Player

TABLE_STATE_SUFFER = 'suffer'
TABLE_STATE_SHOW_HAND = 'show_hand'
TABLE_STATE_INIT = 'init'
class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    MAX_PLAYER = 4
    MIN_PLAYER = 2

    def __init__(self,players):
        self.players = players
        self.deck = None
        self.state = TABLE_STATE_INIT
        self.winner = None

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        pass

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        pass

    def print_players(self):
        print ("Danh sách người chơi")
        for index, player in enumerate(self.players):
            print(f"{index + 1}  {player.name}")

    def total_players(self):
        return len(self.players)

    def list_players(self):
        for index, player in enumerate(self.players):
         print(f"{index + 1}  {player.name}")

    def add_player(self,player):
        if self.total_players() >= self.MAX_PLAYER:
            raise ValueError('Đã tối đa số người chơi')
        self.players.append(player)
    def can_add_player(self):
        return self.total_players() < self.MAX_PLAYER

    def remove_player(self,index):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        if self.total_players() <= self.MIN_PLAYER:
            raise ValueError('Không thể loại bỏ người chơi')
        del self.players[int(index) - 1]
    def can_remove_player(self):
        return self.total_players() > self.MIN_PLAYER

    def deal_card(self):
        '''Chia bài cho người chơi'''
        deck = Deck()
        deck.build()
        deck.shuffle_card()
        self.deck = deck

        for i in range(len(self.players)):
            for n in range(3):
                self.players[i].add_card(deck.deal_card())
        self.state = TABLE_STATE_SUFFER
        print('Đã chia bài xong, mời lật bài')

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        self.show_hand()
        for player in self.players:
            print(player.flip_card())
        print("Người chiến thắng: %s" % self.winner.flip_card())


    def show_hand(self):
        if self.state != TABLE_STATE_SUFFER:
            raise ValueError('Không thể lật bài khi chưa chia bài')

        winner = None  # type: Player
        for player in self.players:
            if not winner:
                winner = player
                continue
            if player.point > winner.point:
                winner = player
            elif player.point == winner.point:
                if player.biggest_card > winner.biggest_card:
                    winner = player
        self.winner = winner
        self.state = TABLE_STATE_SHOW_HAND
def init_table(players) -> Game:
    return Game(players)


def add_new_user() -> Player:
    name_player = input()
    return Player(name_player)