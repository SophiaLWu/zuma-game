# Written in Python 2.7

from Tkinter import *
import ball
import settings
import draw
import random
import math
import copy

def mousePressed(event):
    if canvas.data.fireUserBall == False and canvas.data.isPaused == False \
    and canvas.data.start == False and canvas.data.gameOver == False and \
    canvas.data.winner == False:
        ball.userBall(canvas, event.x, event.y)
    redrawAll()

def keyPressed(event):
    if event.char == 'r':
        settings.init(canvas)
    if event.char == 'p' and canvas.data.start == False and \
    canvas.data.gameOver == False and canvas.data.winner == False:
        canvas.data.isPaused = not canvas.data.isPaused
    if event.keysym == 'Return':
        canvas.data.start = False
    if event.keysym == "space" and canvas.data.start == False and \
    canvas.data.gameOver == False and canvas.data.winner == False and \
    canvas.data.isPaused == False:
        color1 = canvas.data.userBallColor
        color2 = canvas.data.savedUserBallColor
        canvas.data.userBallColor = color2
        canvas.data.savedUserBallColor = color1
    redrawAll()

def checkGameEnd():
    #Checks if any balls reach the black hole. If one does, then game over!
    x1 = canvas.data.endx1
    x2 = canvas.data.endx2
    y1 = canvas.data.endy1
    y2 = canvas.data.endy2
    r = canvas.data.ballRadius
    for ball in canvas.data.balls:
        x = ball[0]
        y = ball[1]
        if (x - r >= x1) and (x + r <= x2) and \
           (y - r >= y1) and (y + r <= y2):
           canvas.data.gameOver = True

def nextLevel():
    #Increments each level by number of balls and speed
    if len(canvas.data.balls) == 0:
        if canvas.data.level == 20:
            canvas.data.winner = True
        else:
            canvas.data.level += 1
            canvas.data.numberBalls += 10
            canvas.data.balls = ball.ballList(canvas)
            if canvas.data.time > 9:
                canvas.data.time -= 2

def doTimerFired():
    canvas.data.counter += 1
    if canvas.data.isPaused == False and canvas.data.start == False and \
    canvas.data.gameOver == False and canvas.data.winner == False:
        if canvas.data.counter % canvas.data.time == 0:
            for b in canvas.data.balls:
                ball.moveBallPosition(canvas, b)
        if canvas.data.fireUserBall == True and \
        canvas.data.userBallHit == False:
            ball.fireUserBall(canvas)
    if canvas.data.fireUserBall == True:
        ball.deleteAddBalls(canvas)
    redrawAll()

def timerFired():
    doTimerFired()
    delay = 1 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def redrawAll():
    canvas.delete(ALL)
    if canvas.data.start == True:
        draw.splashScreen(canvas)
    else:
        drawGame()

def drawGame():
    #This function draws the game
    draw.drawWizard(canvas)
    draw.drawSavedUserBall(canvas)
    draw.drawPath(canvas)
    draw.drawBall(canvas)
    draw.gameInfo(canvas)
    if canvas.data.userBallHit == False:
        draw.drawUserBall(canvas)
    if canvas.data.newUserBall == True:
        ball.newUserBallColor(canvas)
        canvas.data.newUserBall = False
    checkGameEnd()
    nextLevel()
    if canvas.data.gameOver == True:
        draw.gameOverScreen(canvas)
    if canvas.data.winner == True:
        draw.winScreen(canvas)
    if canvas.data.isPaused == True:
        canvas.create_text(canvas.data.canvasWidth/2, 
            canvas.data.canvasHeight/4, text = "PAUSED",
            font = ("Papyrus", 100), fill = 'black')

def run():
    global canvas
    root = Tk()
    canvasWidth = 750
    canvasHeight = 750
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight, \
        highlightthickness = 0)
    canvas["bg"] = "dark khaki"
    canvas.pack()
    class Struct: pass
    canvas.data = Struct()
    canvas.data.canvasWidth = canvasWidth
    canvas.data.canvasHeight = canvasHeight
    settings.init(canvas)
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    root.mainloop()

run()
