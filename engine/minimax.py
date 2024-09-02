import chess
from engine.evaluation import *

def minimax(board: chess.Board, depth: int, alpha: float, beta: float, maximizing_player: bool) -> float:
    '''
    Calculates the best move for a player using the Minimax algorithm with Alpha-Beta pruning.\n
    Returns:
    - `float`: The evaluation score of the best move.
    '''

    # Base case: return the board evaluation if maximum depth is reached or game is over
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')

        # Iterate over all possible legal moves
        for move in board.legal_moves:
            board.push(move)
            # Recursively call minimax for the minimizing player
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()

            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)  # Update alpha with the maximum value found

            # Alpha-Beta pruning: cut off the branch if we find a value worse than beta
            if beta <= alpha:
                break
        
        return max_eval

    else:
        min_eval = float('inf') 

        # Iterate over all possible legal moves
        for move in board.legal_moves:
            board.push(move) 
            # Recursively call minimax for the maximizing player
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()

            min_eval = min(min_eval, eval)
            beta = min(beta, eval)  # Update beta with the minimum value found

            # Alpha-Beta pruning: cut off the branch if we find a value worse than alpha
            if beta <= alpha:
                break
        
        return min_eval
