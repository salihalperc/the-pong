from turtle import Turtle, Screen


class MyLine(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.draw_line()



    def draw_line(self):
        self.pensize(3)
        self.goto(0, -290)
        self.setheading(90)
        for i in range(0, 15):
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)


# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# dashed_line = MyLine()
# dashed_line.draw_line()
# screen.exitonclick()