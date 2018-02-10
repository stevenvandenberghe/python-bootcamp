board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

def draw_board(board):
    for i in range(len(board)):
        if (i + 1) % 3 != 0:
            print(board[i], end='')
        else:
            print(board[i])

def player_input():
    choice = "_"
    while choice[0].lower() != 'x' and choice[0].lower() != 'o':
        choice = input("please input x or o and the location: ")
        print(f'Marker is {choice[0]}, position is {choice[1]}')

def place_marker(board, marker, position):
    pass

draw_board(board)
player_input()