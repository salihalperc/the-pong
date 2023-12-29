from turtle import Turtle, Screen
from scoreboard import Scoreboard
from çzigi import MyLine
from rackets import Rackets
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
my_line = MyLine()
l_score = Scoreboard()
r_score = Scoreboard()
l_racket = Rackets()
r_racket = Rackets()
screen.listen()
screen.onkey(l_racket.move_up, "w")
screen.onkey(l_racket.move_down, "s")
screen.onkey(r_racket.move_up, "Up")
screen.onkey(r_racket.move_down, "Down")

l_racket.go_racket(-350)
r_racket.go_racket(350)



# my_line.draw_line()
r_score.goto_score(20)
l_score.goto_score(-17)


ball = Ball()
ball.make_angle()

is_game_on = True

while is_game_on:
    screen.update()
    ball.move()
    if (ball.xcor() < -385):
        r_score.add_score()
        l_racket.go_racket(-350)
        r_racket.go_racket(350)
        ball.setposition(0, 0)
        ball.dist = 3
        ball.make_angle()
        is_game_on = True

    elif (ball.xcor() > 385):
        l_score.add_score()
        l_racket.go_racket(-350)
        r_racket.go_racket(350)
        ball.setposition(0, 0)
        ball.dist = 3
        ball.make_angle()
        is_game_on = True

    if ball.ycor() < -275 or ball.ycor() > 275:
        ball.detect_wall()

    if (340 - ball.xcor() < 10) or (ball.xcor() - -340 < 10):
        if ball.distance(r_racket) < 50 or ball.distance(l_racket) < 50:
            ball.detect_racket()
            ball.add_speed()






screen.exitonclick()

