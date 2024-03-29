import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score 
score_1 = 0
score_2 = 0

# Gate 1
gate_1 = turtle.Turtle()
gate_1.speed(0)
gate_1.shape("square")
gate_1.shapesize(stretch_wid=5, stretch_len=1)
gate_1.color("yellow")
gate_1.penup()
gate_1.goto(-350, 40)

# Gate 2
gate_2 = turtle.Turtle()
gate_2.speed(0)
gate_2.shape("square")
gate_2.shapesize(stretch_wid=5, stretch_len=1)
gate_2.color("yellow")
gate_2.penup()
gate_2.goto(350, 40)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 30)
ball.xm = -2
ball.ym = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PLAYER_1: 0     PLAYER_2: 0", align="center", font=("Courier", 24, "normal"))

# Moves
# gate_1 up-down

def gate_1_up(): 
    y = gate_1.ycor()
    y += 20
    gate_1.sety(y)

def gate_1_down(): 
    y = gate_1.ycor()
    y -= 20
    gate_1.sety(y)

# gate_2 up-down
def gate_2_up(): 
    y = gate_2.ycor()
    y += 20
    gate_2.sety(y)

def gate_2_down(): 
    y = gate_2.ycor()
    y -= 20
    gate_2.sety(y)


# Keyboard
wn.listen()

# gate_1 up-down
wn.onkeypress(gate_1_up, "w")     
wn.onkeypress(gate_1_down, "s")  
  
# gate_2 up-down
wn.onkeypress(gate_2_up, "Up")     
wn.onkeypress(gate_2_down, "Down")   


# Main game loop
running = True
game_over = False

# def on_close():
#     global running
#     running = False

# wn.onkeypress(on_close, "q")  # Press 'q' to quit
# wn.listen()

while running:
    wn.update()
    time.sleep(0.017)  # Sleep for roughly 60 frames per second

    if not game_over:
        # Move the ball
        ball.setx(ball.xcor() + ball.xm)
        ball.sety(ball.ycor() + ball.ym)

    # Border checking
    # Up and down
    if ball.ycor() > 290:
        ball.sety(290)
        ball.ym *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.ym *= -1    

    # Left and right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.xm *= -1
        score_1 += 1
        pen.clear()
        pen.write("PLAYER_1: {}     PLAYER_2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.xm *= -1
        score_2 += 1
        pen.clear()
        pen.write("PLAYER_1: {}     PLAYER_2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    # Ball and gates
        
    if ball.xcor() > 330 and ball.xcor() < 340 and (ball.ycor() < gate_2.ycor() + 40 and ball.ycor() > gate_2.ycor() - 40):
        ball.setx(330)
        ball.xm *= -1
  
    if ball.xcor() < -330 and ball.xcor() > -340 and (ball.ycor() < gate_1.ycor() + 40 and ball.ycor() > gate_1.ycor() - 40):
        ball.setx(-330)
        ball.xm *= -1

  
     
    if score_1 == 2 or score_2 == 2:
        game_over = True
        pen.clear()
        pen.goto(0,0)
        pen.write("GAME OVER! WE HAVE A WINNER!", align="center", font=("Courier", 24, "normal"))
   

# Close the window gracefully
turtle.mainloop() 