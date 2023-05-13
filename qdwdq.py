import chess
import math

board = chess.Board()

# Define a função de avaliação do tabuleiro
def evaluate_board(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 4,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    score = 0
    for square, piece in board.piece_map().items():
        if piece.color == chess.WHITE:
            score += piece_values.get(piece.piece_type, 0)
        else:
            score -= piece_values.get(piece.piece_type, 0)
    return score

# Define a função de avaliação de cada peça
def evaluate_piece(piece):
    # Implementação simples de avaliação de peças:
    # retorna valores fixos para cada tipo de peça
    piece_values = {"P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 0}
    value = piece_values.get(piece.symbol().upper())
    if piece.color == chess.WHITE:
        return value
    else:
        return -value

# Define a função que escolhe a melhor jogada usando o algoritmo Minimax com poda Alpha-Beta
def choose_move(board, depth):
    def max_value(board, depth, alpha, beta):
        if depth == 0 or board.is_game_over():
            return evaluate_board(board)
        value = -math.inf
        for move in board.legal_moves:
            board.push(move)
            value = max(value, min_value(board, depth - 1, alpha, beta))
            board.pop()
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    def min_value(board, depth, alpha, beta):
        if depth == 0 or board.is_game_over():
            return evaluate_board(board)
        value = math.inf
        for move in board.legal_moves:
            board.push(move)
            value = min(value, max_value(board, depth - 1, alpha, beta))
            board.pop()
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

    best_move = None
    best_score = -math.inf
    alpha = -math.inf
    beta = math.inf
    for move in board.legal_moves:
        board.push(move)
        score = min_value(board, depth - 1, alpha, beta)
        board.pop()
        if score > best_score:
            best_move = move
            best_score = score
        alpha = max(alpha, best_score)
    return best_move

def jogadaIA(board):
        move = choose_move(board, depth=3)
        return move
