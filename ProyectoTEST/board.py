from piece import Piece
from random import random

#Clase donde se crea el tablero, recibe el tamaño y probabilidad de bomba
class Board():
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.lost = False
        self.won = False
        self.numClicked = 0
        self.numNonBoms = 0
        self.setBoard()

    #Funcion que genera el array de dos dimensiones para el tablero
    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                hasBomb = random() < self.prob
                if(not hasBomb):
                    self.numNonBoms +=1
                piece = Piece(hasBomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbors()

    #Funcion que identifica las bombas alrededor
    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row,col))
                piece.setNeighbors(neighbors)

    #Funcion que devuelve una lista de las bombas cercanas en cada casilla
    def getListOfNeighbors(self, index):
        neighbors = []
        for row in range(index[0] -1, index[0]+2):
            for col in range(index[1] -1, index[1]+2):
                outOfBounce = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if (same or outOfBounce):
                    continue
                neighbors.append(self.getPiece((row,col)))
        return neighbors


    def getSize(self):
        return self.size
    
    def getPiece(self, index):
        return self.board[index[0]][index[1]]
    
    #Funciona de la logica de click para identificar acciones dentro de la celda, en caso de dar click y que haya una bomba cambiar el valor de derrota a True
    #Tambien se encuentra implementada la logica de recursividad en caso de no haber bombas alrededor
    def handleClick(self, piece, flag):
        if (piece.getClicked() or (not flag and piece.getFlagged())):
            return
        if (flag):
            piece.toggleFlag()
            return
        piece.click()
        if (piece.getHasBomb()):
            self.lost = True
            return
        self.numClicked += 1
        if (piece.getNumAround() != 0):
            return
        for neighbor in piece.getNeighbors():
            if (not neighbor.getHasBomb() and not neighbor.getClicked()):
                self.handleClick(neighbor, False)

    def getLost(self):
        return self.lost

    #En caso de que la cantidad de celdas descubiertas sea igual a la cantidad de celdas sin bombas devuelve Victoria
    def getWon(self):
        return self.numNonBoms == self.numClicked