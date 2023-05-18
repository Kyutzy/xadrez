import chess
import chess.svg
import time
from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
import cairosvg
from io import BytesIO
import asyncio
import os
from algIa import SelecionaMovimento

board = chess.Board()
print(board)
root = Tk()
root.geometry("425x450")
root.title("Chess")
root.resizable(False, False)

def prepararTabuleiro(board):
    boardPhoto = chess.svg.board(board)
    with open("xadrez.svg", "w") as f:
        f.write(boardPhoto)

    rootUpdater(False)
    root.bind("<Return>", lambda _: enviar())
    
def jogadaPlayer():
  move = jogada.get()
  jogada_entry.delete(0, END)
  move = chess.Move.from_uci(move.lower())
  if move not in board.legal_moves:
    print("Movimento inválido")
    return
  board.push(move)
  rootUpdater(True)

def jogadaIA():
  move = SelecionaMovimento(1, board)
  board.push(move)
  print(board.legal_moves)
  rootUpdater(False)

def enviar():
  if not board.is_game_over():
    if board.turn:
      jogadaPlayer()
    else:
      jogadaIA()
  else:
    print("Fim de jogo")
    print(board.result())
    root.destroy()

def rootUpdater(origem: bool):
  boardPhoto = chess.svg.board(board)
  with open("xadrez.svg", "w") as f:
      f.write(boardPhoto)

  out = BytesIO()
  cairosvg.svg2png(url='xadrez.svg', write_to=out)
  foto = Image.open(out)
  teste = ImageTk.PhotoImage(foto)
  label = Label(master=root, image=teste)
  label.configure(image=teste)
  label.image = teste
  label.place(x=10, y=2)
  jogador.create_oval(5, 5, 25, 25, fill="black") if origem else jogador.create_oval(5, 5, 25, 25, fill="white")
  label.after(150, jogadaIA) if origem else None
  foto.close()

jogada = StringVar()
jogada_entry = Entry(root, textvariable=jogada, width=25, font=("Helvetica", 10))
jogada_entry.place(x=120, y=402)

jogador = Canvas(root, width=25, height=25)
jogador.place(x=375, y=400)
jogador.create_oval(5, 5, 25, 25, fill="white")

orientacao = Label(root, text="Digite sua jogada:", font=("Helvetica", 10))
orientacao.place(x=10, y=400)

texto = Label(root, text="Pressione Enter para enviar")
texto.place(x=10, y=420)


prepararTabuleiro(board)
root.mainloop()