import turtle
import time
import random

r = random

# Creating the screen

turtle_screen = turtle.Screen()
turtle_screen.screensize(canvwidth = 800, canvheight = 800)
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle")

# Creating the turtle

turtle_instance = turtle.Turtle()
turtle_instance.speed(0)
turtle_instance.color("green")
turtle_instance.shape("turtle")
turtle_instance.penup()

# Creating the Writing Turtle

turtle_instance2 = turtle.Turtle()
turtle_instance2.hideturtle()
turtle_instance2.color('black')
turtle_instance2.penup()
style = ('Courier', 30, 'italic')

# Creating the Scoreboard Turtle

turtle_instance3 = turtle.Turtle()
turtle_instance3.hideturtle()
turtle_instance3.color('black')
turtle_instance3.penup()

# Creating the scoreboard

score = 0
timer = 10

def Coordinates(x, y):
    global score
    score += 1

def Turtle3Score():

    global score
    global timer

    if timer == 0:
        turtle_instance3.clear()
        turtle_instance3.write(f"Score: {score}", font=style, align='center')

    else:
        scoreText = f"Score: {score}"
        turtle_instance3.goto(0, 200)
        turtle_instance3.write((scoreText), font=style, align='center')
        turtle_instance3.clear()
        turtle_instance.onclick(Coordinates)
        turtle_instance3.write((scoreText), font=style, align='center')

def Turtle2Timer():
    global timer

    if timer == 0:
        turtle_instance2.clear()
        turtle_instance2.write("Game Over!", font=style, align='center')

    else:
        timerText = f"Time: {timer}"
        turtle_instance2.goto(0, 250)
        turtle_instance2.write((timerText), font=style, align='center')
        turtle_instance2.clear()
        timer -= 1
        turtle_instance2.write((timerText), font=style, align='center')

def TurtlePlay():
    global timer
    global score

    if timer == 0:
        turtle_instance.home()
        Turtle2Timer()
        Turtle3Score()

    else:
        Turtle2Timer()
        Turtle3Score()
        turtle_instance.hideturtle()
        turtle_instance.home()
        turtle_instance.goto(r.randint(-500, 500), r.randint(-500, 500))
        turtle_instance.showturtle()
        time.sleep(1)

while timer >= 0:
    TurtlePlay()

turtle.mainloop()