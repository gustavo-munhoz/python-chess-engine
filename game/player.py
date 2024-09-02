import chess

def get_player_choice():
    print("Which color do you wish to play?")
    print("(1) Whites")
    print("(2) Blacks")
    
    player_team = 0
    while player_team != 1 and player_team != 2:
        try:
            player_team = int(input("Choose an option: "))
            if player_team not in [1, 2]:
                print("Please choose a valid option: 1 (Whites) or 2 (Blacks).")
        except ValueError:
            print("Please enter a number (1 or 2).")
    
    if player_team == 1:
        print("You chose Whites. You'll play first.")
        return chess.WHITE, chess.BLACK
    else:
        print("You chose Blacks. The computer will play first.")
        return chess.BLACK, chess.WHITE

def player_move(board):
    '''Generates and executes a player move based on an keyboard input.'''
    
    move = input("Enter your move in UCI format (e.g., e2e4): ")
    try:
        player_move = chess.Move.from_uci(move)
        if player_move in board.legal_moves:
            board.push(player_move)
        else:
            print("This move is not legal. Try again.")
    except ValueError:
        print("Invalid move format. Please enter a move in UCI format.")
