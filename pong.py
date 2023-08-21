# Import libaries
import turtle
import winsound

# Setup screen
screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.tracer(0)

# Create Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(5, 1)

paddleA.penup()
paddleA.goto(-350, 0)
paddleA.pendown()

# Create Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(5, 1)

paddleB.penup()
paddleB.goto(350, 0)
paddleB.pendown()

# Create the ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")

ball.penup()
ball.goto(0, 0)
ball.pendown()

ball.dx = 1
ball.dy = 1

# Scoreboard
board = turtle.Turtle()
board.speed(0)
board.color("white")

board.penup()
board.hideturtle()
board.goto(0, 260)

board.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# Score
scoreA = 0
scoreB = 0

def paddleA_up():
    paddleA.penup()
    y = paddleA.ycor()
    y += 75
    paddleA.sety(y)

def paddleA_down():
    paddleA.penup()
    y = paddleA.ycor()
    y -= 75
    paddleA.sety(y)

def paddleB_up():
    paddleB.penup()
    y = paddleB.ycor()
    y += 75
    paddleB.sety(y)

def paddleB_down():
    paddleB.penup()
    y = paddleB.ycor()
    y -= 75
    paddleB.sety(y)



# Game loop
while True:
    # Keys
    screen.listen()
    screen.onkeypress(paddleA_up, "w")
    screen.onkeypress(paddleA_down, "s")
    screen.onkeypress(paddleB_up, "Up")
    screen.onkeypress(paddleB_down, "Down")

    screen.update()

    # Move ball
    ball.penup()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking top and bottom
    if ball.ycor() > 290:
        ball.dy *=- 1
    elif ball.ycor() < -290:
        ball.dy *=- 1

    # Border checking left and right
    if ball.xcor() > 350:
        ball.dx *=- 1
        scoreA += 1

        board.clear()
        board.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))

        winsound.PlaySound("pong_sound_effect.wav", winsound.SND_ASYNC)
    elif ball.xcor() < -350:
        ball.dx *=- 1

        scoreB += 1

        board.clear()
        board.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))

        winsound.PlaySound("pong_sound_effect.wav", winsound.SND_ASYNC)
    
    # Return the ball
    if ball.xcor() < -340 and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
        ball.dx *=- 1

        winsound.Beep(500, 50)
    
    elif ball.xcor() > 340 and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
        ball.dx *=- 1

        winsound.Beep(500, 50)