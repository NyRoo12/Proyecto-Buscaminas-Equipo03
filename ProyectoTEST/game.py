import pygame
import os
from time import sleep

#Clase donde se crea el juego y se define la logica de clicks
class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0]//self.board.getSize()[1], self.screenSize[1]//self.board.getSize()[0]
        self.loadImages()

    #Funcion para correr el juego que tambien defiene los eventos de clicks y victoria o derrota
    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()#dibujar el board
            pygame.display.flip()
            if(self.board.getWon()):
                sound = pygame.mixer.Sound("win.wav")
                sound.play()
                sleep(2)
                running = False
        pygame.quit

    #Funcion de dibujado del buscaminas hace uso de la funcion para cargar imagagenes y las posiciona en pantalla
    def draw(self):
        topLeft = (0,0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row,col))
                image = self.getImage(piece)
                #image = self.images["empty-block"]
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    #Funcion para obtener las imagenes, se guardan en base a su nombre para luego ser llamadas
    def loadImages(self):
        self.images = {} #diccionario para mapear
        for fileName in os.listdir("images"): #acceder a carpeta imagenes
            if(not fileName.endswith(".png")):
                continue    
            image = pygame.image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    #Funcion para cargar imagenes en base a lo que se necesite( lo que la celda requiera)
    def getImage(self, piece):
        string = None
        if (piece.getClicked()):
            string = "bomb-at-clicked-block" if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = "flag" if piece.getFlagged() else "empty-block" 
        #string = "unclicked-bomb" if piece.getHasBomb() else str(piece.getNumAround())
        return self.images[string]
    
    #Funcion que de logica del click
    def handleClick(self, position, rightClick):
        if(self.board.getLost()):
            return
        index = position[1] // self.pieceSize[1], position[0]// self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)