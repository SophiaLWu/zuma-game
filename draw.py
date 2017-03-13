import settings
import random
import math

def drawSavedUserBall(canvas):
    #Draws a saved ball that the user can swap at any time.
    offset = canvas.data.canvasHeight/10
    x = canvas.data.canvasWidth/2
    y = canvas.data.canvasHeight/2 + offset
    r = canvas.data.ballRadius/2
    yOffset = offset/20
    canvas.create_oval(x + r + offset/1.5, y + r - yOffset, x - r + offset/1.5, 
        y - r - yOffset, fill = canvas.data.savedUserBallColor, width = 1)
    canvas.create_text(x + offset/2, y, anchor = 'e', text = "Saved ball:", 
        font = ("Papyrus", 18))

def drawUserBall(canvas):
    #This function draws the user ball
    x, y = canvas.data.userBallx, canvas.data.userBally
    r = canvas.data.ballRadius
    canvas.create_oval(x-r, y-r, x+r, y+r, \
        fill = canvas.data.userBallColor, width = 1)

def drawWizard(canvas):
    #Draws around the user ball
    x = canvas.data.canvasWidth/2
    y = canvas.data.canvasHeight/2
    size = canvas.data.ballRadius + 5
    canvas.create_rectangle(x + size, y + size, x - size, y - size, \
        fill = None, width = 2)
    canvas.create_text(x, y - 60, text = "WIZARD", font = ("papyrus", 25))
    x1 = canvas.data.canvasWidth/2 - canvas.data.ballRadius
    y1 = y - 10
    x2 = canvas.data.canvasWidth/2
    y2 = canvas.data.canvasHeight/2 - 50
    x3 = canvas.data.canvasWidth/2 + canvas.data.ballRadius
    y3 = y - 10
    eyeOffset = 10
    eyeRadius = 10
    canvas.create_oval(x + canvas.data.ballRadius, y + canvas.data.ballRadius,
        x - canvas.data.ballRadius, y - canvas.data.ballRadius, fill = None)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3, fill = 'purple')

def gameOverScreen(canvas):
    #Draws game over screen when you lose
    fontSize = canvas.data.canvasWidth/15
    margin = canvas.data.canvasHeight/10
    canvas.create_rectangle(0,0,canvas.data.canvasWidth, 
        canvas.data.canvasHeight, fill = 'black')
    canvas.create_text(canvas.data.canvasWidth/2, canvas.data.canvasHeight/4,
        text = "YOUR LANDS HAVE BEEN", 
        font = ("Papyrus", fontSize), fill = "red")
    canvas.create_text(canvas.data.canvasWidth/2, 
        canvas.data.canvasHeight/4 + margin,
        text = "SENTENCED TO PERIL.", 
        font = ("Papyrus", fontSize), fill = "red")
    canvas.create_text(canvas.data.canvasWidth/2, 
        canvas.data.canvasHeight * 2/3,
        text = "GAME OVER", 
        font = ("Papyrus", fontSize*2), fill = "white")
    canvas.create_text(canvas.data.canvasWidth/2, 
        canvas.data.canvasHeight * 2/3 + margin,
        text = "Press R to restart", 
        font = ("Papyrus", fontSize), fill = "white")

def winScreen(canvas):
    #Draws win screen when you beat all 20 levels
    fontSize = canvas.data.canvasWidth/15
    margin = canvas.data.canvasHeight/10
    canvas.create_text(canvas.data.canvasWidth/2, canvas.data.canvasHeight/4,
        text = "YOU HAVE SAVED YOUR", 
        font = ("Papyrus", fontSize))
    canvas.create_text(canvas.data.canvasWidth/2, 
        canvas.data.canvasHeight/4 + margin,
        text = "LANDS FROM GREAT PERIL!", 
        font = ("Papyrus", fontSize))
    canvas.create_text(canvas.data.canvasWidth/2, 
        canvas.data.canvasHeight * 2/3,
        text = "YOU WIN!!", 
        font = ("Papyrus", fontSize*2))
    canvas.create_text(canvas.data.canvasWidth/2, 
        canvas.data.canvasHeight * 2/3 + margin,
        text = "Press R if you want to do it again.", 
        font = ("Papyrus", fontSize))

def drawPath(canvas):
    #This function draws the white path that the balls roll along
    drawEnd(canvas)
    indent = 2*canvas.data.ballRadius*3
    edge = canvas.data.ballRadius/2.5
    r = canvas.data.ballRadius + 2
    canvas.create_line(0, indent, canvas.data.canvasWidth - indent + 2*r + edge, 
        indent, fill = "white", width = 2*r)
    canvas.create_line(canvas.data.canvasWidth - indent + r + edge, indent,
        canvas.data.canvasWidth - indent + r + edge, 
        canvas.data.canvasHeight - indent + r + edge, 
        fill = "white", width = 2*r)
    canvas.create_line(canvas.data.canvasWidth - indent + 2*r + edge,
        canvas.data.canvasHeight - indent + edge, indent - 2*r, 
        canvas.data.canvasHeight - indent + edge, fill = "white", width = 2*r)
    canvas.create_line(indent - r, canvas.data.canvasHeight - indent + edge,
        indent - r, 2*indent - r, fill = "white", width = 2*r)
    canvas.create_line(indent - 2*r, 2*indent,
        canvas.data.canvasWidth - 2*indent + 2*r + edge, 
        2*indent, fill = "white", width = 2*r)
    canvas.create_line(canvas.data.canvasWidth - 2*indent + r + edge, 
        2*indent, canvas.data.canvasWidth - 2*indent + r + edge, 
        canvas.data.canvasHeight - 2*indent + r + edge, 
        fill = "white", width = 2*r)
    canvas.create_line(canvas.data.canvasWidth - 2*indent + 2*r + edge, 
        canvas.data.canvasHeight - 2*indent + edge, 2*indent - 2*r, 
        canvas.data.canvasHeight - 2*indent + edge, 
        fill = "white", width = 2*r)
    canvas.create_line(2*indent - r, canvas.data.canvasHeight - 2*indent + edge, 
        2*indent - r, 3*indent + r, 
        fill = "white", width = 2*r)

def drawEnd(canvas):
    #This function draws the ending black hole
    indent = 2*canvas.data.ballRadius*3
    edge = canvas.data.ballRadius/2.5
    r = canvas.data.ballRadius + 2
    x1 = 2*indent - 2*r
    y1 = 3*indent - r 
    x2 = x1 + 2*r
    y2 = y1 + 2*r
    canvas.create_oval(x1, y1, x2, y2, fill = 'black', outline = 'black',
        width = 16)
    canvas.data.endx1 = x1
    canvas.data.endy1 = y1
    canvas.data.endx2 = x2
    canvas.data.endy2 = y2

def drawBall(canvas):
    #This draws each ball
    r = canvas.data.ballRadius
    for ball in canvas.data.balls:
        canvas.create_oval(ball[0] - r, ball[1] - r, ball[0] + r, ball[1] + r,
            fill = ball[2], width = 1) 

def splashScreen(canvas):
    #This is the starting splash screen
    titleText = canvas.data.canvasWidth * 1/4
    subText = canvas.data.canvasWidth * 1/25
    underTitle = canvas.data.canvasWidth * 1/10
    canvas.create_text(canvas.data.canvasWidth/2, canvas.data.canvasHeight/6,
        text = "ZUMA", font = ("Papyrus", titleText), fill = "white")
    canvas.create_text(canvas.data.canvasWidth/2, canvas.data.canvasHeight/6 +
        underTitle, text = "(ultra lite 2.0)", font = ("Papyrus", subText), 
        fill = "white")
    instructions(canvas)

def instructions(canvas):
    #Creates the instructions text
    topMargin = 3.0 * canvas.data.canvasHeight/10
    rightMargin = canvas.data.canvasWidth/6
    leftMargin = canvas.data.canvasWidth - rightMargin
    edge = canvas.data.canvasHeight/30
    height = 6*canvas.data.canvasHeight/9.2
    canvas.create_rectangle(rightMargin, topMargin, leftMargin, 
        topMargin + height, fill = None, width = 2, outline = "brown")
    text = canvas.data.canvasWidth * 1/50
    canvas.create_text(canvas.data.canvasWidth/2, 
        canvas.data.canvasHeight * 1/3,
        text = "Game Instructions", font = ("Papyrus", 2*text), fill = "brown")
    canvas.create_text(canvas.data.canvasWidth/2, 
        canvas.data.canvasHeight * 1/3,
        text = """
    Welcome to the lands of Zuma! Dark magic has plagued your lands and you 
    must save them. Evil sorcerors have enchanted colored balls to move in a 
    maze-like structure towards a black pit. If any colored balls reach the 
    black pit, your lands are doomed! In order to rid your lands of this dark 
    magic, you need to eliminate all the enchanted colored balls before any 
    reach the pit. Since there are 20 sorcerors, you must do this 20 times.

    You are a wizard! So you have the ability to shoot randomly colored balls 
    from the center towards the balls. Right-click to fire a ball in the 
    direction of your cursor. When there is a group of 3 or more balls of the 
    same color touching, all of those balls disappear! Any balls that are 
    remaining in the front roll back to connect with the other balls. Press 
    SPACE to swap out your ball with a saved one. You may save only 1 ball.

    There are 20 levels ("sorcerors"). If you can beat them all, you win and 
    thus save your lands! (Note: It's hard, so you're doomed for failure.)
    Press ENTER to start the game, P to pause, and R to restart the game.

    Hint: You can shoot balls offscreen if you don't like the ball color
        """,
         font = ("Papyrus", text), fill = "brown", anchor = "n")

def gameInfo(canvas
    ):
    fontSize = canvas.data.canvasWidth/25
    margin = canvas.data.canvasHeight/15
    canvas.create_text(canvas.data.canvasWidth/5, margin,
        text = "Level: %d" % (canvas.data.level), font = ("Papyrus", fontSize),
        anchor = 'w')
    canvas.create_text(canvas.data.canvasWidth * 4/5, margin,
        text = "Balls left: %d" % len(canvas.data.balls),
        font = ("Papyrus", fontSize), anchor = 'e')