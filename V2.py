import os
import shutil
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]
def display_board(board):
    rows = len(board)
    terminal_width = shutil.get_terminal_size().columns
    padding = (terminal_width - 9) // 2
    for row in board:
        print(" "*padding + " | ".join(row))
        rows -= 1
        if (rows >= 1):
            print((padding-1)*" " + "-----------")
    print("-" * terminal_width)
display_board(board)
def get_player_move(letter):
    while True:
        try:
            move = int(input(f"Player, which cell (1-9) do you want to place {letter} on?:\n"))
            if move in range(1, 10): 
                return move
            else:
                print("That's not a valid cell. Please choose a number from 1 to 9.")
        except ValueError:
            print("That's not even a number. You okay over there?")
def place_move(board,letter):
    move = get_player_move(letter)
    if (board[(move-1)//3][(move-1)%3] == 'X' or board[(move-1)//3][(move-1)%3] == 'O'):
        print("Cell already used")
        place_move(board,letter)
        return
    board[(move-1)//3][(move-1)%3] = letter
    display_board(board)
def board_done(board):

    for i in board:
        for j in i:
            if j.isdigit():
                return False
    print("Full Board")
    return True
def check_board(board):
    for i in board:
        if ("".join(i) == "XXX"):
            print("X wins! game over")
            return True
        if ("".join(i) == "OOO"):
            print("O wins! game over")
            return True
    for i in range(3):
        if (board[0][i] == board[1][i] == board[2][i]):
            if not board[0][i] == "":
                if board[0][i] == "X":
                    print("X wins! game over")
                    return True
                if board[0][i] == "O":
                    print("O wins! game over")
                    return True
    if board[0][0] == board[1][1] == board[2][2]:
        if not board[1][1] == "5":
                if board[0][0] == "X":
                    print("X wins! game over")
                    return True
                if board[0][0] == "O":
                    print("O wins! game over")
                    return True
    if board[0][2] == board[1][1] == board[2][0]:
        if not board[1][1] == "5":
                if board[0][2] == "X":
                    print("X wins! game over")
                    return True
                if board[0][2] == "O":
                    print("O wins! game over")
                    return True

while (True):
    while (not(board_done(board))):
        move1 = place_move(board,'X')
        if(check_board(board)):
            break
        if (board_done(board)):
            print("Game over!")
            break
        move2 = place_move(board,'O')
        if(check_board(board)):
            break
    while True:
        replay = input("Wanna go again? (Y/N)")
        if (replay != 'Y' and replay != 'N'):
            print("Enter Y or N.")
            continue
        break
    if replay == 'N':
        break
    else:
        
        board = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        os.system('cls' if os.name == 'nt' else 'clear')
        print("New Game")
        display_board(board)
