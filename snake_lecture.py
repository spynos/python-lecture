import turtle
import time
import random

game_over = False

# Screen setting
win = turtle.Screen()
win.title("SNAKE")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Make snake's head
head = turtle.Turtle()
head.shape("turtle")
head.color("yellow")
head.penup()
head.goto(0, 0)

# Change head direction
def turn_right():
    head.setheading(0)
def turn_up():
    head.setheading(90)
def turn_left():
    head.setheading(180)
def turn_down():
    head.setheading(270)

# Key mapping - turing snake
win.onkeypress(turn_up, "Up")
win.onkeypress(turn_down, "Down")
win.onkeypress(turn_right, "Right")
win.onkeypress(turn_left, "Left")
win.listen()

# Move snake
def move():
    head.forward(20)

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.penup()
food.shapesize(0.5, 0.5)
food.goto(200, 0)

# Segments
segments = []
def add_segment():
    new = turtle.Turtle()
    new.shape("circle")
    new.color("grey")
    new.penup()
    segments.append(new)

# Game_over
def game_over():
    ending = turtle.Turtle()
    ending.penup()
    ending.color("red")
    ending.hideturtle()
    ending.write("Game Over", align="center", font=("Arial", 50))
    del head

# Score
score = 0
board = turtle.Turtle()
board.penup()
board.color("white")
board.hideturtle()
board.goto(200, 270)

# Main game loop
while True:
    move()
    time.sleep(0.1)
    win.update()
    board.clear()
    board.write("score: {}".format(score), font = ("Arial", 20))

    # Check for head collision
    for segment in segments:
        if segment.distance(head) < 15:
            game_over()
    
    #Make new food after eat!
    if head.distance(food) < 20:
        x = random.randint(-390, 390)
        y = random.randint(-290, 290)
        food.goto(x, y)
        add_segment()
        score = score + 20

    # Move segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    # First segments -> follow head
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())



    

                
    
        
       


