"""
Tetris Clone
------------
Write a Tetris clone
"""

import PySimpleGUI as sg      

from random import seed
from random import randint
from datetime import datetime

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
TILE_SIZE = 25
TILE_MARGIN = 2

board = list()
level = 1
piecesMax = 7
currentPace = 200
fallingPiece = oldPiece = canvas = window = None
oldCol = oldRow = 0
points = 0

pieceColor = {
    0: "black", #Empty cell
    1: "gold",#The "O", square or "Smashboy"piece 
    2: "dark turquoise",  #The "I", stick or "Hero" piece
    3: "red3",   #The "Z", dog left or "Cleveland Z" piece
    4: "lime green", #The "S", dog right or "Rhode Island Z" piece
    5: "dark violet",#The "T" or "Teewee" piece
    6: "orange red",#The "L", periscope left or "Orange Ricky" piece
    7: "medium blue"   #The "J", periscope right or "Blue Ricky" piece
}

pieceMap = {
    #The "O" or square piece
    1: [
        [1,1],
        [1,1]],
    #The "I" of stick piece
    2: [
        [2],
        [2],
        [2],
        [2]],
    #The "Z", dog looking left or "Cleveland Z" piece
    3: [
        [0,3,3],
        [3,3,0]],
    #The "S", dog looking right or "Rhode Island Z" piece
    4: [
        [4,4,0],
        [0,4,4]],
    #The "T" or "Teewee" piece
    5: [
        [5,5,5],
        [0,5,0]],
    #The "L", periscope looking left or "Orange Ricky" piece
    6: [
        [0,6],
        [0,6],
        [6,6]],
    #The "J", periscope looking right or "Blue Ricky" piece
    7: [
        [7,0],
        [7,0],
        [7,7]]
}

def initGame():
    seed(datetime.now())


def initBoard():
    global board 

    board = [[0 for j in range(BOARD_WIDTH)] for i in range(BOARD_HEIGHT)]


def matrixWidth(piece):
    return len(piece[0])


def matrixHeight(piece):
    return len(piece)


def showPiece(text,piece):
    height = matrixHeight(piece)
    width = matrixWidth(piece)

    print(text)
    print("    ",end="")
    for j in range(width):
        print("[{}]".format(j),end="")
    print(end="\n")
    for i in range(height):
        print("[{}]".format(i),end=" ")
        for j in range(width):
            print(" {} ".format(piece[i][j]),end="")
        print(end="\n")


def drawWindow():
    global window, canvas

    canvasWidth = BOARD_WIDTH*(TILE_SIZE+TILE_MARGIN*2)
    canvasHeight = BOARD_HEIGHT*(TILE_SIZE+TILE_MARGIN*2)
    layout = [      
                [sg.Graph(canvas_size=(canvasWidth, canvasHeight), graph_bottom_left=(0,0), graph_top_right=(canvasWidth,canvasHeight), background_color='black', key='CANVAS')],      
                [sg.Text("Points: {}".format(points), key='POINTS', size=[30,1])],
                [sg.Text("Level: {}".format(level), key='LEVEL', size=[30,1])] 
            ]      
    window = sg.Window('Tetris Clone', layout, return_keyboard_events=True)      
    window.Finalize()      
    canvas = window['CANVAS']


def drawBoard():
    global board, canvas

    xpos = 0
    ypos = 0
    height = matrixHeight(board)
    width = matrixWidth(board)
    canvas.Erase()
    for j in range(width):
        xpos += TILE_MARGIN
        for i in range(height):
            ypos += TILE_MARGIN
            canvas.DrawRectangle(
                [xpos,ypos],
                [xpos+TILE_SIZE,ypos+TILE_SIZE], 
                fill_color=pieceColor[board[i][j]], 
                line_color="gray2"
            )
            ypos += TILE_SIZE+TILE_MARGIN
        else: 
            ypos = 0
            xpos += TILE_SIZE+TILE_MARGIN


def rotatePiece(piece):
    width = matrixWidth(piece)
    height = matrixHeight(piece)

    newPiece = [[0 for j in range(height)] for i in range(width)]

    for j in range(width):
        for i in range(height):
            newPiece[j][height-i-1] = piece[i][j]

    return newPiece


def pickAPiece():
    pick = randint(1,piecesMax)
    piece = pieceMap[pick]
    rotate = maxRotate = 0
    if pick >= 2 and pick <= 5: maxRotate = 1
    if pick >= 6: maxRotate = 2    
    rotate = randint(0,maxRotate)
    for i in range(rotate):
        piece = rotatePiece(piece)

    return piece


def hasRoom(piece,Col,Row):
    Room = True

    pieceHeight = matrixHeight(piece)
    pieceWidth = matrixWidth(piece)

    if (Row-pieceHeight+1 < 0 ): 
        Room = False
        return Room

    boardCut = [[board[Row-i][Col+j] for j in range(pieceWidth)] for i in range(pieceHeight)]

    for i in range(pieceHeight):
        for j in range (pieceWidth):
            if (piece[i][j] != 0): 
                if (boardCut[i][j] !=0 ): 
                    Room = False
    return Room


def placePiece(piece,Col,Row):
    global board, oldCol, oldRow, oldPiece
    placed = True

    if Row != BOARD_HEIGHT-1:
        oldPieceHeight = matrixHeight(oldPiece)
        oldPieceWidth = matrixWidth(oldPiece)

        for i in range(oldPieceHeight) :
            for j in range(oldPieceWidth):
                if oldPiece[i][j] != 0: 
                    board[oldRow-i][oldCol+j] = 0                         

    if (oldRow!=Row) and (not hasRoom(piece,Col,Row)): 
        placed = False
        piece = oldPiece
        Col = oldCol
        Row = oldRow

    pieceHeight = matrixHeight(piece)
    pieceWidth = matrixWidth(piece)

    for i in range(pieceHeight):
        for j in range(pieceWidth):
                if board[Row-i][Col+j] == 0 and piece[i][j] != 0: 
                    board[Row-i][Col+j] = piece[i][j]

    oldCol = Col
    oldRow = Row
    oldPiece = piece
    return placed


def deleteLine(lineNumber):
    global board, points, level, window, currentPace

    points += 100
    if points % 1000 == 0: 
        level += 1
        currentPace -= int(currentPace*0.1)
    window['POINTS'].update("Points: {}".format(points))
    window['LEVEL'].update("Level: {}".format(level))
    for i in range(lineNumber,BOARD_HEIGHT-3):
        for j in range(BOARD_WIDTH):
            board[i][j] = board[i+1][j]
    for j in range(BOARD_WIDTH): board[BOARD_HEIGHT-1][j] = 0


def checkLinesOnBoard():
    global board

    scanComplete = False
    i = 0
    while not scanComplete:
        countNoZeros=0
        for j in range(BOARD_WIDTH):
            if board[i][j] > 0: countNoZeros+=1
        if countNoZeros == 10: deleteLine(i)
        else: i+=1
        if i==BOARD_HEIGHT: scanComplete = True


def gameLoop():
    global fallingPiece, currentPace, oldRow, points, level
    clockcount = 0
    refreshInterval = 10
    fallingCol = fallingRow = 0
    currentPace //= level

    while True:      
        # Event Capture
        event, values = window.read(timeout=refreshInterval)      
        if event == sg.WIN_CLOSED:      
            break  
        if event == "Left:113":
            if fallingCol>0: fallingCol-=1
        if event == "Right:114":
            if fallingPiece != None: 
                fallingPieceWidth = matrixWidth(fallingPiece)
                if fallingCol<BOARD_WIDTH-fallingPieceWidth: fallingCol+=1
        if event == "Up:111":
            if fallingPiece != None: 
                fallingPiece = rotatePiece(fallingPiece)
                fallingPieceWidth = matrixWidth(fallingPiece)
                fallingPieceHeight = matrixHeight(fallingPiece)
                if fallingCol+fallingPieceWidth>BOARD_WIDTH: fallingCol=BOARD_WIDTH-fallingPieceWidth
                if fallingRow-fallingPieceHeight<0: fallingRow=fallingPieceHeight
        if event == "space:65":
            while placePiece(fallingPiece,fallingCol,fallingRow): fallingRow-=1

        # Game Logic
        if not fallingPiece:
            checkLinesOnBoard()
            fallingPiece = pickAPiece()
            fallingCol = (BOARD_WIDTH // 2 - len(fallingPiece) // 2)
            fallingRow = BOARD_HEIGHT-1    
            oldRow = fallingRow    
            if not hasRoom(fallingPiece,fallingCol,fallingRow):
                sg.Popup("Game Over!")
                break
        if not placePiece(fallingPiece,fallingCol,fallingRow): fallingPiece = None
        if clockcount >= currentPace: 
            fallingRow-=1
            clockcount=0
        else: clockcount += refreshInterval
        drawBoard()
    window.Close()  


def main():
    initGame()
    initBoard()
    drawWindow()
    gameLoop()


if __name__=="__main__":
    main()