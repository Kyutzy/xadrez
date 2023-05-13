import socket
import threading
import chess
import random
import os
import asyncio

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtém o nome da máquina local
host = 'localhost'
#print(socket.gethostbyname(socket.gethostname()))

port = 9999
pool = []
# Associa a porta
s.bind((host, port))

# Escutando...
s.listen(5)

board = chess.Board()


        
def jogo(connection : socket.socket):
    print('iniciei')
    connection.send('Oi, já lido com você, pode falar comigo'.encode('utf-8'))
    while True:
        mensagem = connection.recv(1024)
        print(mensagem.decode('utf-8'))
        connection.send('OK'.encode('utf-8'))
        print()


def jogada(connection : tuple, inicio:int):
    while True:
        connection[inicio].send('receive'.encode('utf-8'))
        connection[inicio].recv(1024).decode('utf-8')
        connection[inicio].send(f'Sua vez de jogar, seus movimentos possíveis são: {board.legal_moves}'.encode('utf-8'))
        connection[inicio].send('write'.encode('utf-8'))
        movimento = connection[inicio].recv(1024).decode('utf-8')
        board.push_san(movimento)
        os.system('cls')
        for con in connection:
            con.send('board'.encode('utf-8'))
            con.send(f'{movimento}'.encode('utf-8'))
            con.recv(1024)
        print(board)
        #connection[inicio].send('board'.encode('utf-8'))
        inicio = 1 if board.turn == chess.WHITE else 0

while True:
    # Estabelece conexão com o cliente
    c, addr = s.accept()
    pool.append(c)
    print('Conexão de', addr)
    if len(pool) == 2:
        threading.Thread(target=jogada, args=(pool, random.randint(0,1),)).start()

        
    

