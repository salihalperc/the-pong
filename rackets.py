from turtle import Turtle, Screen


class Rackets(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        # self.setheading(90)


    def go_racket(self, position_x):
        self.penup()
        self.goto(position_x, 0)
        self.showturtle()


    def move_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)
        # self.forward(20)

    def move_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)
        # self.backward(20)


# screen = Screen()
# screen.setup(800, 600)
# screen.bgcolor("black")
# racket = Rackets()
# racket.go_racket(370)
# screen.exitonclick()