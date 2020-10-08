"""
Memory Game
-------------
Write a memory game.
"""

import PySimpleGUI as sg      

from random import seed
from random import randint
from datetime import datetime


def initGame():
    global max_rows, max_cols
    max_rows = 1
    max_cols = 1
    seed(datetime.now())
    while max_rows % 2 != 0:
        max_rows=randint(2,8)
    while max_cols % 2 != 0:
        max_cols=randint(4,8)

def shuffleNumbers():
    elements=max_cols*max_rows//2
    numbers=[i for i in range(1,elements+1)]
    for j in range(elements):
        k=randint(0,elements-1)
        numbers[j],numbers[k]=numbers[k],numbers[j]
    return numbers

def initBoard():
    global board
    board = [[0 for i in range(max_rows)] for j in range(max_cols)]
    values=shuffleNumbers()
    for i in range(max_rows):
        for j in range(max_cols):
            if len(values)==0: values = shuffleNumbers()
            board[j][i] = values.pop()

def drawWindow():
    global window
    layout =  [[sg.Button('?', size=(4, 2), key=(i,j), pad=(0,0), button_color=('white','grey')) for j in range(max_cols)] for i in range(max_rows)]
    window = sg.Window('Memory Game', layout)      
    window.Finalize()      

def isDone():
    done = True
    for i in range(max_rows):
        for j in range(max_cols):
            if board[j][i] > 0: done = False
    return done

def gameLoop():
    pick = 0
    count = 0
    firstCard = secondCard = None
    firstValue = secondValue = firstCol = secondCol = firstRow = secondRow = 0
    while True:      
        event, values = window.read()      
        if event == sg.WIN_CLOSED:      
            break     
        if board[event[1]][event[0]]!=0:
            if pick == 1:
                if (event != firstCard):
                    secondCard = event
                    secondRow = event[0]
                    secondCol = event[1]
                    secondValue = board[event[1]][event[0]]
                    if (firstValue == secondValue):
                        window[firstCard].update(firstValue, button_color=('white','red'))
                        window[secondCard].update(secondValue, button_color=('white','red'))    
                        board[firstCol][firstRow] = 0
                        board[secondCol][secondRow] = 0
                    else:
                        window[event].update(board[event[1]][event[0]], button_color=('white','black'))
                    count+=1
                    pick = 2                    
            else:
                if (firstValue != secondValue) and (firstValue != 0) and (secondValue !=0):
                    window[firstCard].update("?", button_color=('white','grey'))
                    window[secondCard].update("?", button_color=('white','grey'))                
                firstCard = event
                firstRow = event[0]
                firstCol = event[1]
                firstValue = board[event[1]][event[0]]
                window[event].update(board[event[1]][event[0]], button_color=('white','black'))
                pick = 1
        if isDone():
            sg.popup("It took you {} guesses.".format(count),title="Done!")
            break
    window.close()

def main():
    initGame()
    initBoard()
    drawWindow()
    gameLoop()

if __name__ == "__main__":
    main()
