import game

def print_menu(table):
    print(f"""================================
    1 - Danh sách người chơi 
    2 - Thêm người chơi mới {"(có thể thêm)" if table.can_add_player() else "(đã tối đa người chơi)"}
    3 - Loại người chơi {"(có thể loại)" if table.can_remove_player() else "(số người chơi tối thiểu rồi)"} 
    4 - Chia bài {"(có thể chia)"}
    5 - Lật bài {"(chưa chia bài)" if table.state != game.TABLE_STATE_SUFFER else "(có thể chia bài)"}
    6 - Xem lại game vừa chơi
    7 - Xem lịch sử hôm nay
    8 - Công an tới, tốc biến
    ================================
>""")


def print_welcome():
    print("""Welcome!!!
Chào mừng đến với game đánh bài ba lá ( vui thôi nhá )
Có bao nhiêu người muốn chơi:""")   

def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    print_welcome()
    number_players = input()
    if not number_players.isdigit() or not (2 <= int(number_players) <= 8):
        print('Giá trị đầu vào không hợp lệ')
        exit(0)

    number_players = int(number_players)
    init_number_players = []
    for i in range(number_players):
        print(f'Tên người chơi {i + 1}')
        init_number_players.append(game.add_new_user())

    table = game.init_table(init_number_players)

    while True:
        print_menu(table)
        user_input = input()
        # validate
        if not user_input.isdigit() or not (1 <= int(user_input) <= 8):
            print('Giá trị đầu vào không hợp lệ')
            continue
        user_input = int(user_input)

        if user_input == 1:
            table.print_players()

        elif user_input == 2:
            print(f'Tên người chơi')
            table.add_player(game.add_new_user())

        elif user_input == 3:
            table.print_players()
            print('Nhập id người chơi bạn muốn loại')
            remove_id = input()
            if not remove_id.isdigit() or not (1 <= int(remove_id) <= table.total_players()):
                print('Giá trị đầu vào không hợp lệ')
                continue
            table.remove_player(remove_id)

        elif user_input == 4:
            table.deal_card()

        elif user_input == 5:
            table.flip_card()

        elif user_input == 6:
            print('Chưa kết nối được database')

        elif user_input == 7:
            print('Chưa kết nối được database')

        elif user_input == 8:
            exit(1)




if __name__ == '__main__':
    main()
