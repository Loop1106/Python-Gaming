# importing turtle
import turtle

# importing random
from random import *


# importing math
import math


# creating screen
wn = turtle.Screen()
wn.bgpic("bg.gif")
wn.setup(650,600)


# register_shape images
turtle.register_shape("enemy.gif")

# creating square wall
wall = turtle.Turtle()
wall.pencolor("brown")
wall.pensize(10)
wall.speed(0)
wall.penup()
wall.setposition(-290,290)
wall.pendown()


for sides in range(4):
    wall.fd(570)
    wall.lt(270)
wall.hideturtle()

# score
score = 0

# drawing the score
scorep=turtle.Turtle()
scorep.speed(0)
scorep.color("white")
scorep.penup()
scorep.setposition(-200,260)
scorestring="Score: %s" %score
scorep.write(scorestring,False,align="right",font=("Matura MT Script Capitals", 15, "normal"))
scorep.hideturtle()

# creating fire
fire=turtle.Turtle()
fire.shape("triangle")
fire.color("yellow")
fire.penup()
fire.setheading(90)
fire.speed(0)
fire.shapesize(0.5,0.5)
fire.setposition(0,-400)
fire.hideturtle()

# state of fire
firestate = "ready"
# speed of fire
s_fire = 20


# creating player
player = turtle.Turtle()
player.shape("triangle")
player.color("yellow")
player.speed(0)
player.penup()
player.setheading(90)
player.setposition(-50,50)
# speed of player
p_speed = 2

shape = 1
# creating numbers of enemies
number_of_enemies = 1

# creating list
enemies = []

for j in range(1,number_of_enemies+1):
    enemies.append(turtle.Turtle())

for enemy in enemies:

    # creating enemy
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.speed(0)
    x = randint(-270,270)
    y = randint(-270,270)
    enemy.setposition(x , y)


# creating collision
def collision(a1,a2):
    distance = math.sqrt(math.pow(a1.xcor() - a2.xcor(),2) + math.pow(a1.ycor() - a2.ycor(),2) )
    if distance < 18:
        return True
    else:
        return False


# on_up key
def on_up():
    player.setheading(90)

# on_down key
def on_down():
    player.setheading(270)


# on_right key
def on_right():
    player.setheading(0)


# on_left key
def on_left():
    player.setheading(180)


def on_speed():
    global p_speed
    p_speed += 0.5

def original_speed():
    global p_speed
    p_speed = 2

# listening from the keyboard
wn.listen()
wn.onkeypress(on_up, "Up")
wn.onkeypress(on_down, "Down")
wn.onkeypress(on_right, "Right")
wn.onkeypress(on_left, "Left")
wn.onkey(on_speed, "space")
wn.onkey(original_speed, "o")

# main loop
while True:
    player.fd(p_speed)
    if player.ycor() > 275:
        p_speed = 0
        # display game over
        g = turtle.Turtle()
        g.color("orange")
        g.penup()
        g.setposition(-2, 0)
        string = "You Crashed The Wall"
        g.write(string, False, align="center", font=("serif", 20, "bold"))
        g.hideturtle()

    if player.ycor() < -265:
        p_speed = 0
        # display game over
        g = turtle.Turtle()
        g.color("orange")
        g.penup()
        g.setposition(-2, 0)
        string = "You Crashed The Wall"
        g.write(string, False, align="center", font=("serif", 20, "bold"))
        g.hideturtle()


    if player.xcor() < -275:
        p_speed = 0
        # display game over
        g = turtle.Turtle()
        g.color("orange")
        g.penup()
        g.setposition(-2, 0)
        string = "You Crashed The Wall"
        g.write(string, False, align="center", font=("serif", 20, "bold"))
        g.hideturtle()


    if player.xcor() > 265:
        p_speed = 0
        # display game over
        g = turtle.Turtle()
        g.color("orange")
        g.penup()
        g.setposition(-2, 0)
        string = "You Crashed The Wall"
        g.write(string, False, align="center", font=("serif", 20, "bold"))
        g.hideturtle()

    for enemy in enemies:
        if collision(player,enemy):
            p_speed += 0.2
            score += 2
            scorep.setposition(-200, 260)
            scorep.clear()
            scorestring = "Score: %s" % score
            scorep.write(scorestring, False, align="right", font=("Matura MT Script Capitals", 15, "normal"))
            x = randint(-270, 270)
            y = randint(-270, 270)
            enemy.setposition(x, y)


turtle.done()


