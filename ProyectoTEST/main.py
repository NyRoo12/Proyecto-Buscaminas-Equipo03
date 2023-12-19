from game import Game
from board import Board

#Script principal donde se genera todo
size= (10,10) #tamaño del buscaminas
prob = 0.12 #probabilidad de que se encuentre una bomba en la celda
board = Board(size,prob) #creacion del tablero

screenSize = (400,400) #tamaño pantalla
game = Game(board,screenSize) #creacion del juego e inicio de este

game.run()