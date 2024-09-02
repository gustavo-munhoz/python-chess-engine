import chess
from engine.minimax import minimax

def get_best_move(board: chess.Board, depth):
    '''Calculates and returns the best move in relation to parameter `depth`.'''
    best_move = None
    best_value = float('-inf') if board.turn == chess.WHITE else float('inf')
    
    for move in board.legal_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, float('-inf'), float('inf'), not board.turn)
        board.pop()

        # The best move for whites is the largest positive number.
        if board.turn == chess.WHITE:
            if board_value > best_value:
                best_value = board_value
                best_move = move
        
        # The best move for blacks is the largest negative number.
        else: 
            if board_value < best_value:
                best_value = board_value
                best_move = move
    
    return best_move