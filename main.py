from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    ### Collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    ### Collision with paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    ### Detect no collision
    
    # R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    #L Paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()