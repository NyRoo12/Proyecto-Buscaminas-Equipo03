#Clase para la definir el contenido de las celdas, recibe un bool si tiene bomba
class Piece():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False

    def getHasBomb(self):
        return self.hasBomb

    def getClicked(self):
        return self.clicked
    
    def getFlagged(self):
        return self.flagged
    
    #Define el numero en caso de ser celda limpia e identifica bombas alrededor
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumAround()

    #Define cantidad dde bombas alrededor de la casilla
    def setNumAround(self):
        self.numAround = 0
        for piece in self.neighbors:
            if(piece.getHasBomb()):
                self.numAround += 1

    def getNumAround(self):
        return self.numAround
    
    #Marca celda con banderda
    def toggleFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True

    def getNeighbors(self):
        return self.neighbors