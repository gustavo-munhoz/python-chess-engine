from art import *
from game.board_manager import initialize_board, display_board
from game.player import get_player_choice, player_move
from game.move_generator import get_best_move


tprint("IACHESS")

board = initialize_board()
display_board(board)

player_color, computer_color = get_player_choice()

while not board.is_game_over():
    if board.turn == player_color:
        player_move(board)        

    else:
        print("Computer's move:")
        computer_move = get_best_move(board, depth=6)
        board.push(computer_move)
    
    display_board(board)

print("Game over!")
result = board.result()

if result == "1-0":
    print("White wins!")

elif result == "0-1":
    print("Black wins!")

else:
    print("It's a draw.")
    