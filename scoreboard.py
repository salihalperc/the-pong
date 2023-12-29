from turtle import Screen, Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0



    def add_score(self):
        self.clear()
        self.score += 1
        self.write_score()


    def goto_score(self, position_x):
        self.goto(position_x, 260)
        self.write_score()

    def write_score(self):
        self.write(self.score, False, "center", ('Arial', 30, 'normal'))






#
# screen = Screen()
# screen.bgcolor("black")
# scoreboard = Scoreboard()
# scoreboard.goto_score(30)
# screen.exitonclick()

