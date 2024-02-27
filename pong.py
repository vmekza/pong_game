import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)




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
gate_2.goto(340, 40)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 30)

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
def on_close():
    global running
    running = False

wn.onkeypress(on_close, "q")  # Press 'q' to quit
wn.listen()

while running:
    wn.update()
    time.sleep(0.017)  # Sleep for roughly 60 frames per second

# Close the window gracefully
wn.bye()