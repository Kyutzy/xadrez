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

    out = BytesIO()
    cairosvg.svg2png(url='xadrez.svg', write_to=out)
    foto = Image.open(out)
    teste = ImageTk.PhotoImage(foto)
    foto.close()
    label = Label(master=root, image=teste)
    label.configure(image=teste)
    label.image = teste
    label.place(x=10, y=2)

    jogada_enviar = Button(root, text="Enviar", command=lambda: enviar(), width=10, font=("Helvetica", 10))
    jogada_enviar.place(x=450, y=425)
    root.bind("<Return>", lambda _: enviar())
    

def enviar():
  if board.turn:
    move = jogada.get()
    jogada_entry.delete(0, END)
    move = chess.Move.from_uci(move)
    if move not in board.legal_moves:
      print("Movimento inválido")
      return
  else:
    move = SelecionaMovimento(3, board)
    print(move)
  board.push(move)
  print(board.legal_moves)
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
  foto.close()



jogada = StringVar()
jogada_entry = Entry(root, textvariable=jogada, width=50, font=("Helvetica", 10))
jogada_entry.place(x=0, y=400)


prepararTabuleiro(board)
root.mainloop()