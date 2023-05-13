import chess
import os


prioridades = {
    chess.PAWN: [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0],

    chess.KNIGHT: [-50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50],

    chess.BISHOP: [-20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20],

    chess.ROOK: [0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0],

    chess.QUEEN: [-20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20],

    chess.KING: [20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]
                    }
board = ""
def quantidadePecas():
    pecas = [(board.piece_at(peca).symbol(), board.piece_at(peca).color) for peca in board.piece_map()]
    numeroPecas = {'r': 0, 'b': 0, 'k': 0, 'q': 0, 'n': 0, 'p': 0, 'N': 0, 'P': 0, 'R': 0, 'B': 0, 'K': 0, 'Q': 0}
    for peca in pecas:
        numeroPecas[peca[0]] += 1
    print(numeroPecas)
    return numeroPecas

def avaliaPeca(peca):
    valorPeca = sum([prioridades[peca][i] for i in board.pieces(peca, chess.WHITE)])
    valorPeca = valorPeca + sum([-prioridades[peca][chess.square_mirror(i)]
                            for i in board.pieces(peca, chess.BLACK)])
    return (peca, valorPeca)

def avaliaTabuleiro():
  if board.is_checkmate():
        return -9999
  if board.is_stalemate():
        return 0
  if board.is_insufficient_material():
        return 0


  numeroPecas = quantidadePecas()
  material = 100 * (numeroPecas['p'] - numeroPecas['P'])+ 320 * (numeroPecas['n'] - numeroPecas['N']) + 330 * (numeroPecas['b'] - numeroPecas['B']) + 500 * (numeroPecas['r'] - numeroPecas['R']) + 900 * (numeroPecas['q'] - numeroPecas['Q'])

  cadaPeca = [avaliaPeca(peca) for peca in prioridades]
  
  avalia = material + sum([i[1] for i in cadaPeca])
  return -avalia

def BuscaEmProfundidade(alpha, beta):
    avaliacao = avaliaTabuleiro()
    if (avaliacao >= beta):
        return beta
    if (avaliacao > alpha):
        alpha = avaliacao

    for move in list(board.legal_moves):
        if board.is_capture(move):
            board.push(move)
            pontuacao = -BuscaEmProfundidade(-beta, -alpha)
            board.pop()
            if (pontuacao >= beta):
                return beta
            if (pontuacao > alpha):
                alpha = pontuacao
    return alpha

def SelecionaMovimento(depth, tabuleiro):
    global board
    board = tabuleiro
    MelhorMovimento = chess.Move.null()
    MelhorValor = -os.sys.maxsize
    alpha = -os.sys.maxsize
    beta = os.sys.maxsize
    for movimento in list(board.legal_moves):
        board.push(movimento)
        boardValor = -alphabeta(-beta, -alpha, depth - 1)
        if boardValor > MelhorValor:
            MelhorValor = boardValor
            MelhorMovimento = movimento
        if boardValor > alpha:
            alpha = boardValor
        board.pop()
    return MelhorMovimento

def alphabeta(alpha, beta, depthleft):
    MelhorPontuacao = -9999
    if (depthleft == 0):
        return BuscaEmProfundidade(alpha, beta)
    for movimento in list(board.legal_moves):
        board.push(movimento)
        pontuacao = -alphabeta(-beta, -alpha, depthleft - 1)
        board.pop()
        if (pontuacao >= beta):
            return pontuacao
        if (pontuacao > MelhorPontuacao):
            MelhorPontuacao = pontuacao
        if (pontuacao > alpha):
            alpha = pontuacao
    return MelhorPontuacao
    