# importing turtle
import turtle

# importing random
from random import randint

# importing math
import math

# importing os
import os

wn = turtle.Screen()

wn.setup(700, 650)
wn.bgpic('bg.gif')
wn.title('ATTACK GAME')

# register shape
turtle.register_shape("enemy.gif")
turtle.register_shape("player.gif")
turtle.register_shape("bullet.gif")


# score
score = 0

# drawing the score
scorep = turtle.Turtle()
scorep.speed(0)
scorep.color("white")
scorep.penup()
scorep.setposition(-210, 265)
scorestring = "Score: %s" % score
scorep.write(scorestring, False, align="right", font=("Matura MT Script Capitals", 20, "normal"))
scorep.hideturtle()

# life
lifes = 5
# drawing the life
life = turtle.Turtle()
life.speed(0)
life.color("white")
life.penup()
life.setposition(-100, 270)
lifestring = "life: %s" % lifes
life.write(lifestring, False, align="right", font=("Britannic Bold", 20, "normal"))
life.hideturtle()

# playerspeed
p_speed = 20

# enemyspeed
enemyspeed = 2

# firespeed
firespeed = 30

# fire state
firestate = "ready"

# player
player = turtle.Turtle()
player.setheading(90)
player.shape("player.gif")
player.color('red')
player.speed(20)
player.penup()
player.setposition(0, -220)

# creating fire
fire = turtle.Turtle()
fire.shape("bullet.gif")
fire.color("yellow")
fire.penup()
fire.setheading(90)
fire.speed(0)
fire.shapesize(0.5, 0.5)
fire.setposition(0, -400)
fire.hideturtle()




# number of enemies
num_of_enemies = 5

# creating empty list
enemies = []

# adding enemies to list
for j in range(num_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.shape("enemy.gif")
    enemy.shapesize(2, 2)
    enemy.penup()
    enemy.color("blue")
    enemy.speed(0)
    x = randint(-500, -100)
    y = randint(-50, 50)
    enemy.setposition(x, y)


# on left key
def left():
    x = player.xcor()
    x -= p_speed
    if x < -315:
        x = -315
    player.setx(x)


# on right key
def right():
    x = player.xcor()
    x += p_speed
    if x > 308:
        x = 308
    player.setx(x)


# on fire key
def fires():
    global firestate
    if firestate == "ready":
        #os.system("bullet.wav&")
        firestate = "fire"
        x = player.xcor()
        y = player.ycor() + 50
        fire.setposition(x, y)
        fire.showturtle()


# creating collision
def collision(a1, a2):
    d = math.sqrt(math.pow(a1.xcor() - a2.xcor(), 2) + math.pow(a1.ycor() - a2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False


# listening the keyboard
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(fires, "space")

# main loop
while True:
    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()
        x += enemyspeed
        if x > 320:
            lifes -= 1
            lifestring = "life: %s" % lifes
            life.clear()
            life.write(lifestring, False, align="right", font=("Britannic Bold", 20, "normal"))
            life.hideturtle()
            # resetting enemy position
            x = randint(-500, -100)
            y = randint(-50, 50)
            enemy.setposition(x, y)

        enemy.setx(x)

        if lifes <= 0:
            enemyspeed = 0
            fire.hideturtle()
            firespeed = 0
            p_speed = 0
            # display game over
            g = turtle.Turtle()
            g.color("orange")
            g.penup()
            g.setposition(-2, 0)
            string = "Game Over"
            g.write(string, False, align="center", font=("Magneto", 50, "bold"))
            g.hideturtle()

            # displaying the score after the game over
            scorep.setposition(100, -50)
            scorep.color("white")
            scorestring = "Your Score is : %s" % score
            scorep.clear()
            scorep.write(scorestring, False, align="right", font=("Old English Text MT", 16, "bold"))
            break

        # checking for collision between fie and enemy
        if collision(fire, enemy):
            # reset the fire
            fire.hideturtle()
            firestate = "ready"

            fire.setposition(0, -400)

            # reset the enemy
            x = randint(-500, -100)
            y = randint(-50, 50)
            enemy.setposition(x, y)

            # increasing the score
            score += 5
            #os.system("score.mp3&")
            scorestring = "Score: %s" % score
            scorep.clear()
            scorep.write(scorestring, False, align="right", font=("Matura MT Script Capitals", 20, "normal"))

            # increasing the speed of enemy from 20 upto 50 by 5
            if score >= 15 and 50:
                enemyspeed += 1

            # increasing the speed of enemy from 55 upto 100 by 10
            if score >= 55 and 100:
                enemyspeed += 2


    # move the fire up
    if firestate == "fire":
        y = fire.ycor()
        y += firespeed
        fire.sety(y)

    # where the fire come back, will come back after reached 100 of y
    if fire.ycor() > 100:
        fire.hideturtle()
        firestate = "ready"

turtle.done()










