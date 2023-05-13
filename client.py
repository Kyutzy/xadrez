import socket
import os
import chess
# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtém o nome da máquina local
host = '192.168.148.24'

port = 9999
board = chess.Board()
# Conecta ao servidor
s.connect((host, port))
print(f'-\n{board}\n-\n')


def boardHandler(s):
    message = s.recv(1024)
    board.push_san(message.decode('utf-8'))
    os.system('cls')
    print(board)
    s.send('OK'.encode('utf-8'))

def writeHandler(s):
    msg = input()
    print(msg)
    s.send(msg.encode('utf-8'))

def receiveHandler(s):
    s.send('OK'.encode('utf-8'))
    message = s.recv(1024)
    print(message.decode('utf-8'))

protocolo = {
    'board': boardHandler,
    'write': writeHandler,
    'receive' : receiveHandler,
    'OK' : lambda: print('OK')
}

while 1:
    msg = s.recv(1024).decode('utf-8')
    protocolo[msg](s)
    

