import settings
import random
import math
import copy

def userBall(canvas, x,y):
    #This function calculates how the user ball moves when the user clicks 
    #at a location
    canvas.data.fireUserBall = True
    xStart = canvas.data.canvasWidth/2
    yStart = canvas.data.canvasHeight/2
    xDistance = abs(x - xStart)
    yDistance = abs(y - yStart)
    velocity = 20
    if xDistance == 0:
        canvas.data.userBallDx = 0
        if y < yStart: 
            canvas.data.userBallDy = -velocity
        elif y > yStart:
            canvas.data.userBallDy = velocity
    elif yDistance == 0:
        canvas.data.userBallDy = 0
        if x < xStart: 
            canvas.data.userBallDx = -velocity
        elif x > xStart:
            canvas.data.userBallDx = velocity
    elif xDistance != 0 and yDistance != 0:
        userBallAtAngle(canvas, x, y, xStart, yStart, 
                        xDistance, yDistance, velocity)

def userBallAtAngle(canvas, x, y, xStart, yStart, 
                    xDistance, yDistance, velocity):
    angle = math.atan2(yDistance, xDistance)
    dx = math.cos(angle) #Trig! Used so that whatever angle you shoot,
    dy = math.sin(angle) #the ball moves at same velocity
    if x < xStart and y < yStart:
        canvas.data.userBallDx = -dx*velocity
        canvas.data.userBallDy = -dy*velocity
    elif x < xStart and y > yStart:
        canvas.data.userBallDx = -dx*velocity
        canvas.data.userBallDy = dy*velocity
    elif x > xStart and y < yStart:
        canvas.data.userBallDx = dx*velocity
        canvas.data.userBallDy = -dy*velocity
    elif x > xStart and y > yStart:
        canvas.data.userBallDx = dx*velocity
        canvas.data.userBallDy = dy*velocity

def fireUserBall(canvas):
    #This function actually moves the user ball after it has been fired
    #If the ball goes off screen, a new ball resets to the center
    r = canvas.data.ballRadius
    canvas.data.userBallx += canvas.data.userBallDx
    canvas.data.userBally  += canvas.data.userBallDy
    if canvas.data.userBallx - r < 0 or canvas.data.userBally - r< 0 or \
    canvas.data.userBallx + r > canvas.data.canvasWidth or \
    canvas.data.userBally + r > canvas.data.canvasHeight:
        restartUserBall(canvas)

def restartUserBall(canvas):
    #Makes a new ball to fire at the center
    canvas.data.userBallx = canvas.data.canvasWidth/2
    canvas.data.userBally = canvas.data.canvasHeight/2
    canvas.data.userBallDx = 0
    canvas.data.userBallDy = 0
    canvas.data.newUserBall = True
    canvas.data.userBallHit = False
    canvas.data.fireUserBall = False

def hitBall(canvas, x, y, userBallx, userBally):
    #Checks to see whether or not the userball hits something with x/y coords
    if abs(x - userBallx) <= 2*canvas.data.ballRadius and \
    abs(y - userBally) <= 2*canvas.data.ballRadius:
        return True
    return False

def moveBallsBack(canvas, i):
    #When the user ball inserts, this function allows the rest of the balls
    #to be moved up one to account for the inserted user ball
    for index in xrange(i,-1,-1):
        dx, dy = findBallPosition(canvas, canvas.data.balls[index])
        canvas.data.balls[index][0] += dx
        canvas.data.balls[index][1] += dy

def deleteAddBalls(canvas):
    #This function inserts the user balls and deletes balls if conditions
    #are met.
    if canvas.data.fireUserBall == True:
        for i in xrange(len(canvas.data.balls)): #Iterate through all balls
            x = canvas.data.balls[i][0]
            y = canvas.data.balls[i][1]
            ballColor = canvas.data.balls[i][2]
            userColor = canvas.data.userBallColor
            userBallx = canvas.data.userBallx
            userBally = canvas.data.userBally
            if hitBall(canvas, x, y, userBallx, userBally) == True:
                num = findIndexAndInsert(canvas, i, userBallx, x, y, userColor)
                restartUserBall(canvas)
                delete3ColorBallsInRow(canvas, num)
                return

def findIndexAndInsert(canvas, i, userBallx, x, y, userColor):
    canvas.data.userBallHit = True
    #if/elif statements determines on which side of the ball you
    #hit gets the new ball.
    if userBallx <= x:
        addedUserBall = [x, y, userColor]
        num = i+1
        canvas.data.balls.insert(num, addedUserBall)
        moveBallsBack(canvas, num-1)
    elif userBallx > x:
        dx, dy = findBallPosition(canvas, canvas.data.balls[i])
        addedUserBall = [x+dx, y+dy, userColor]
        num = i
        canvas.data.balls.insert(num, addedUserBall)
        moveBallsBack(canvas, num-1)
    return num

def delete3ColorBallsInRow(canvas, index):
    #This function is the helper for deleteAddBalls() that determines whether
    #or not there are 3 same color balls in the row and deletes those balls
    start, end = findPopBallIndices(canvas, index)
    currentState = copy.deepcopy(canvas.data.balls)
    if end - start >= 2:
        listPoppedBalls = [] #Keep the list of popped ball locations
        for num in xrange(start, end + 1): #Will use this list for joining
            x = currentState[num][0]
            y = currentState[num][1]
            cords = [x,y]
            listPoppedBalls.append(cords)
        canvas.data.balls[start:end+1] = []
        joinBalls(canvas, start, end, listPoppedBalls) #Need to put balls back together

def findPopBallIndices(canvas, index):
    start = 0
    end = 0
    rightIndex = index-1
    leftIndex = index+1
    color = canvas.data.balls[index][2]
    goingRight = True
    goingLeft = True
    while goingRight == True: #Iterates to the front of list
        if (rightIndex < 0) or (canvas.data.balls[rightIndex][2] != color):
            goingRight = False
        rightIndex -= 1
    while goingLeft == True: #Iterates to the back of list
        if (leftIndex >= len(canvas.data.balls)) or \
        (canvas.data.balls[leftIndex][2] != color):
            goingLeft = False
        leftIndex += 1
    start = rightIndex + 2 #Actual start index of ball that needs to be deleted
    end = leftIndex - 2 #Actual ending index of ball that needs to be deleted
    return start, end

def joinBalls(canvas, start, end, poppedList):
    #This function joins the chain of balls back together after there have
    #been balls that are deleted
    currentState = copy.deepcopy(canvas.data.balls)
    numBalls = end - start + 1
    movedList = []
    for index in xrange(start - 1, -1, -1):
        movedList.append(currentState[index])
    poppedList.reverse()
    if start > 0:
        if start < numBalls:
            endPopped = -1
        else:
            endPopped = start - numBalls - 1
        for i in xrange(start-1, endPopped, -1): #First put balls in the
            ball = canvas.data.balls[i]          #position that popped
            poppedI = start - 1 - i              #balls were
            ball[0] = poppedList[poppedI][0]
            ball[1] = poppedList[poppedI][1]
        if start > numBalls: #If there are still balls left to move
            for j in xrange(endPopped, -1, -1):  #Then, put the rest of the
                ball = canvas.data.balls[j]      #balls in moved up positions
                movedI = endPopped - j
                ball[0] = movedList[movedI][0]
                ball[1] = movedList[movedI][1]
    if start < len(canvas.data.balls): #Make sure that the index exists
        delete3ColorBallsInRow(canvas, start)
    #Recursion call above. If balls are joined and at least 3 of the
    #newly joined balls have the same color, then pop again, and then join.
    #Base case is when there aren't >=3 joined balls of the same color

def newUserBallColor(canvas):
    #This function finds a random color for the user ball
    randomIndex = random.randint(0, len(canvas.data.ballColors) - 1)
    canvas.data.userBallColor = canvas.data.ballColors[randomIndex]

def randomSavedBallColor(canvas):
    #This function finds a random color for the saved ball (to start)
    randomIndex = random.randint(0, len(canvas.data.ballColors) - 1)
    return canvas.data.ballColors[randomIndex]

def ballList(canvas):
    #This function makes a list of a set # of balls that start in a line
    #off the screen to the left
    diameter = 2*canvas.data.ballRadius
    ballList = []
    x = -canvas.data.ballRadius
    y = 2*canvas.data.ballRadius*3 
    for i in xrange(canvas.data.numberBalls):
        randomIndex = random.randint(0, len(canvas.data.ballColors) - 1)
        color = canvas.data.ballColors[randomIndex]
        newBall = [x,y,color]
        ballList.append(newBall)
        x -= diameter
    return ballList

def findBallPosition(canvas, ball):
    #This function determines the direction of movement of the balls along the
    #path and returns the dx and dy
    dxBalls = 0
    dyBalls = 0
    indent = 2*canvas.data.ballRadius*3
    if ball[0] < canvas.data.canvasWidth - indent and ball[1] < indent+1:
        dxBalls = canvas.data.ballRadius*2
    elif ball[1] < canvas.data.canvasHeight - indent and \
    ball[0] > canvas.data.canvasWidth - indent:
        dyBalls = canvas.data.ballRadius*2
    elif ball[0] > indent and ball[1] > canvas.data.canvasHeight - indent:
        dxBalls = -canvas.data.ballRadius*2
    elif ball[0] < indent and ball[1] > 2*indent:
        dyBalls = -canvas.data.ballRadius*2
    elif ball[1] <= 2*indent and ball[0] < canvas.data.canvasWidth - 2*indent:
        dxBalls = canvas.data.ballRadius*2
    elif ball[0] > canvas.data.canvasWidth - 2*indent and \
    ball[1] < canvas.data.canvasHeight - 2*indent:
        dyBalls = canvas.data.ballRadius*2
    elif ball[1] > canvas.data.canvasHeight - 2*indent and \
    ball[0] > 2*indent:
        dxBalls = -canvas.data.ballRadius*2
    elif ball[0] < 2*indent and ball[1] > 3*indent:
        dyBalls = -canvas.data.ballRadius*2
    return dxBalls, dyBalls

def moveBallPosition(canvas, ball):
    #This function moves each ball by the dx and dy found in the previous
    #function each time the timer fires.
    dx, dy = findBallPosition(canvas, ball)
    ball[0] += dx
    ball[1] += dy

def ballColors():
    #This function returns the possible colors of the balls
    return ['red', 'gold', 'blue2', 'springgreen']
