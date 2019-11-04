import turtle
import time
import random

# Screen setting
win = turtle.Screen()
win.title("SNAKE") #창제목
win.bgcolor("black") #배경색상
win.setup(width=600, height=600)
win.tracer(0) #화면에 그림 그려지는 과정이 보이지 않도록

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
    time.sleep(3)
    win.bye()


# Score board
score = 0
board = turtle.Turtle()
board.penup()
board.color("white")
board.hideturtle()
board.goto(0, 270)

# Main game loop
while True:
    move()
    time.sleep(0.1)
    win.update()
    board.clear()
    board.write("score: {}".format(score), align="center", font = ("Arial", 20))

    # Check for head collision
    for segment in segments:
        if segment.distance(head) < 15:
            game_over()
    
    # Make new food after eat!
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y) #화면 중 랜덤 위치에 뿌리기
        add_segment() #먹이 먹을 때마다 몸통 한칸 추가
        score = score + 20 #먹이 먹을 때마다 점수 20점

    # Move segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    # First segments -> follow head
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())



    

                
    
        
       


