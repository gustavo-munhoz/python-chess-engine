import chess

def evaluate_board(board) -> int:
    '''Calculates the estimated advantage for each color.\n
    If `return value` is greater than 0, whites are in advantage.\n
    If `return value` is less than 0, blacks are in advantage.
    '''

    # Powerful pieces have more value.
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    evaluation = 0

    for piece_type in piece_values:
        evaluation += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        evaluation -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]

    evaluation += calculate_center_control_bonus(board)
    evaluation += calculate_mobility_bonus(board)
    evaluation += calculate_piece_position_bonus(board)
    
    return evaluation

def calculate_center_control_bonus(board: chess.Board) -> int:
    '''Calculates a bonus considering how many pieces are in the center squares for each color.'''

    bonus = 0
    center_squares = [chess.E4, chess.D4, chess.E5, chess.D5]
    center_control_bonus = 0.5
    for square in center_squares:
        piece = board.piece_at(square)
        if piece:
            if piece.color == chess.WHITE:
                bonus += center_control_bonus

            else:
                bonus -= center_control_bonus

    return bonus

def calculate_mobility_bonus(board: chess.Board) -> int:
    '''Calculates a bonus considering how many legal moves each color has.'''

    bonus = 0
    white_mobility = len(list(board.legal_moves)) if board.turn == chess.WHITE else 0
    black_mobility = len(list(board.legal_moves)) if board.turn == chess.BLACK else 0

    bonus += 0.1 * white_mobility
    bonus -= 0.1 * black_mobility

    return bonus

def calculate_piece_position_bonus(board: chess.Board) -> int:
    '''Calculates a bonus regarding piece positions.\n
    Knights generate a bonus if they are positioned in the center squares.\n
    Rooks generate a bonus if it has an empty line to move.
    '''

    def is_open_file(board: chess.Board, rook_square) -> bool:
        file_index = chess.square_file(rook_square)
        for rank in range(8):
            square = chess.square(file_index, rank)
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.PAWN:
                return False
        
        return True
    
    center_squares = [chess.E4, chess.D4, chess.E5, chess.D5]    
    bonus = 0

    for knight in board.pieces(chess.KNIGHT, chess.WHITE):
        if knight in center_squares:
            bonus += 0.3

    for knight in board.pieces(chess.KNIGHT, chess.BLACK):
        if knight in center_squares:
            bonus -= 0.3

    for rook in board.pieces(chess.ROOK, chess.WHITE):
        if is_open_file(board, rook):
            bonus += 0.5

    for rook in board.pieces(chess.ROOK, chess.BLACK):
        if is_open_file(board, rook):
            bonus -= 0.5
    
    return bonus