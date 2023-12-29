from turtle import Turtle, Screen
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.7, 0.7)
        self.angle = self.heading()
        self.make_angle()
        self.dist = 3



    def make_angle(self):
        self.angle = random.randint(0, 360)
        self.setheading(self.angle)
        if self.angle == 90 or self.angle == 270 or self.angle == 180 or self.angle == 0:
            self.make_angle()


    def detect_wall(self):
        if 0 < self.heading() < 90:
            self.right(2*(self.heading()))
        elif 90 < self.heading() < 180:
            self.left(2*(180-self.heading()))
        elif 180 < self.heading() < 270:
            self.right(2*(self.heading()-180))
        else:
            self.left(2*(360-self.heading()))


    def move(self):
        self.forward(self.dist)


    def detect_racket(self):
        self.forward(0)
        if 0 < self.heading() < 90:
            # self.left(2 * (90-self.heading()))
            self.setheading(random.randint(91, 179))
        elif 90 < self.heading() < 180:
            # self.right(2 * (self.heading() - 90))
            self.setheading(random.randint(1, 89))
        elif 180 < self.heading() < 270:
            # self.left(2 * (270 - self.heading()))
            self.setheading(random.randint(271, 359))
        else:
            # self.right(2 * (360 - self.heading()))
            self.setheading(random.randint(181, 269))
        self.move()


    def add_speed(self):
        self.dist += 0.3


