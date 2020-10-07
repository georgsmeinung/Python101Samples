"""
Bouncing ball
-------------
Write a program that displays a bouncing ball.
"""
import PySimpleGUI as sg      

from random import choice
from random import seed
from random import randint
from datetime import datetime

def resetBall(xsize=400,ysize=400,radius=25):
    global xpos, ypos, xspeed, yspeed, xaccel, yaccel, xdirection, ydirection, maxx, maxy, ballradius

    maxx=xsize
    maxy=ysize
    ballradius=radius

    seed(datetime.now())
    xpos=randint(0+ballradius,maxx-ballradius)
    ypos=randint(0+ballradius,maxy-ballradius)

    seed(datetime.now())
    xspeed=randint(1,ballradius)
    xaccel=xspeed
    yspeed=randint(1,ballradius)
    yaccel=yspeed

    seed(datetime.now())
    xdirection=choice([-1,1])
    ydirection=choice([-1,1])

def drawWindow():
    global window, canvas, ball

    layout = [      
                [sg.Graph(canvas_size=(maxx, maxy), graph_bottom_left=(0,0), graph_top_right=(maxx,maxy), background_color='white', key='CANVAS')],      
                [sg.Button('Slower', key='SLOW'), 
                sg.Button('Faster', key='FAST'),
                sg.Button('Restart', key='RESET')
                ]      
            ]      
    window = sg.Window('Bouncing Ball', layout)      
    window.Finalize()      
    canvas = window['CANVAS']
    ball = canvas.DrawCircle((xpos,ypos), ballradius, fill_color='black',line_color='white')

def calculatePostion():
    global xpos, ypos, xspeed, yspeed, xdirection, ydirection

    xposnew=xpos+(xspeed*xdirection) 
    yposnew=ypos+(yspeed*ydirection) 
    if xposnew<0 or xposnew>maxx-ballradius*2:
        xdirection*=-1
    if yposnew<0 or yposnew>maxy-ballradius*2:
        ydirection*=-1
    return int(xposnew),int(yposnew)

def bounce():
    global xpos, ypos, xspeed, yspeed

    resetBall()
    drawWindow()
    while True:      
        event, values = window.read(timeout=100)      
        if event == sg.WIN_CLOSED:      
            break      
        if event == 'SLOW':      
            if xspeed>0: xspeed-=xaccel      
            if yspeed>0: yspeed-=yaccel
        if event == 'FAST':      
            xspeed+=xaccel
            yspeed+=yaccel
        if event == 'RESET': resetBall()
        xpos, ypos = calculatePostion()
        canvas.RelocateFigure(ball,xpos,ypos+ballradius*2)

if __name__ == "__main__":
    bounce()
