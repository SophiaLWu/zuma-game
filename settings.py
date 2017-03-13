import ball

def init(canvas):
    canvas.data.ballRadius = 20
    canvas.data.numberBalls = 30
    canvas.data.ballColors = ball.ballColors()
    canvas.data.counter = 0
    canvas.data.balls = ball.ballList(canvas)
    canvas.data.userBallx = canvas.data.canvasWidth/2
    canvas.data.userBally = canvas.data.canvasHeight/2
    canvas.data.userBallDx = 0
    canvas.data.userBallDy = 0
    canvas.data.fireUserBall = False
    canvas.data.userBallColor = canvas.data.ballColors[0]
    canvas.data.userBallHit = False
    canvas.data.newUserBall = True
    canvas.data.isPaused = False
    canvas.data.start = True
    canvas.data.gameOver = False
    canvas.data.level = 1
    canvas.data.time = 48
    canvas.data.winner = False
    canvas.data.savedUserBallColor = ball.randomSavedBallColor(canvas)