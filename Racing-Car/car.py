# importing turtle
import turtle


# importing random
from random import randint


# importing math
import math


# title of the game
turtle.title("RACING CAR")
# creating screen
wn = turtle.Screen()
wn.bgpic("bg.gif")
wn.setup(800,600)

# register_shape images
turtle.register_shape("car1.gif")
turtle.register_shape("car.gif")
turtle.register_shape("car3.gif")

# score
score = 0

# drawing the score
scorep=turtle.Turtle()
scorep.speed(0)
scorep.color("white")
scorep.penup()
scorep.setposition(-120,250)
scorestring="Score: %s" %score
scorep.write(scorestring,False,align="right",font=("Matura MT Script Capitals", 20, "normal"))
scorep.hideturtle()




# speed of player
p_speed = 40

# creating player
player = turtle.Turtle()
player.shape("car.gif")
player.penup()
player.speed(0)
player.setposition(-27,-230)



# fire state
firestate="ready"

# the speed of all cars
enemy_speed = 10

# number of cars
num_of_enemies=2

# part two of cars
num_of_enemies2=3

# creating empty list
enemies=[]

# part two creating list
enemies2=[]


# adding enemies to list
for j in range(num_of_enemies):
    enemies.append(turtle.Turtle())
# giving part one cars same image car
for enemy in enemies:
    enemy.shape("car1.gif")
    enemy.shapesize(2,2)
    enemy.penup()
    enemy.color("blue")
    enemy.speed(0)
    x=randint(-240,240)
    y=randint(100,650)
    enemy.setposition(x,y)


# part two creating another three cars
for j in range(num_of_enemies2):
    enemies2.append(turtle.Turtle())
# part two giving the cars same image car
for enemy2 in enemies2:
    enemy2.shape("car3.gif")
    enemy2.shapesize(2,2)
    enemy2.penup()
    enemy2.color("blue")
    enemy2.speed(0)
    x=randint(-200,200)
    y=randint(350,700)
    enemy2.setposition(x,y)




# Pressing on right key
def on_right():
    x = player.xcor()
    x += p_speed
    if x > 240:
        x = 240
    player.setx(x)

# Pressing on left key
def on_left():
    x = player.xcor()
    x -= p_speed
    if x < -240:
        x = -240
    player.setx(x)


# creating collision
def collision(a1,a2):
    d = math.sqrt(math.pow(a1.xcor()-a2.xcor(),2)+math.pow(a1.ycor()-a2.ycor(),2))
    if d  < 50:
        return True
    else:
        return False

def change():
    x=randint(-200,200)
    y=randint(350,700)
    enemy2.setposition(x,y)

# listening the keyboard
turtle.listen()
turtle.onkey(on_right, "Right")
turtle.onkey(on_left, "Left")
turtle.onkey(change, "a")


# main loop
while True:
    # part one walking all the brown cars
    for enemy in enemies:
        #move the enemy
        y=enemy.ycor()
        y-=enemy_speed

        if y < - 320:
            score += 2
            # displaying the score
            scorep.setposition(-120,250)
            scorep.color("white")
            scorestring ="Score is : %s" % score
            scorep.clear()
            scorep.write(scorestring,False,align="right",font=("Matura MT Script Capitals", 20, "normal"))
            x = randint(-240, 240)
            y = randint(150, 650)
            enemy.setposition(x, y)
        enemy.sety(y)

        # increasing the speed of enemy from 20 upto 50 by 5
        if score >= 15 and 50:
            enemy_speed += 0.2



        # checking for collision between player and brown cars
        if collision(player, enemy):
            enemy_speed = 0
            p_speed = 0


            # display game over
            g = turtle.Turtle()
            g.color("yellow")
            g.penup()
            g.setposition(-2, 0)
            string = "Game Over"
            g.write(string, False, align="center", font=("times new roman", 50, "bold"))
            g.hideturtle()
            break
    # walking all the teal cars
    for enemy2 in enemies2:
        #move the enemy
        y=enemy2.ycor()
        y-=enemy_speed

        # if teal cars reached 290 of y will miss
        if y < - 320:
            score += 2
            # displaying the score
            scorep.setposition(-120,250)
            scorep.color("white")
            scorestring ="Score is : %s" % score
            scorep.clear()
            scorep.write(scorestring,False,align="right",font=("Matura MT Script Capitals", 20, "normal"))
            x = randint(-240, 240)
            y = randint(150, 650)
            enemy2.setposition(x, y)
        enemy2.sety(y)

        # checking for collision between player and teal cars
        if collision(player, enemy2):
            enemy_speed = 0
            p_speed = 0

            # display game over
            g = turtle.Turtle()
            g.color("yellow")
            g.penup()
            g.setposition(-2, 0)
            string = "Game Over"
            g.write(string, False, align="center", font=("times new roman", 50, "bold"))
            g.hideturtle()
            break




























turtle.done()
