########################################################################
##
# CS 101
# Program #
# Name
# Email
#
# PROBLEM : Describe the problem
#
# ALGORITHM :
#      1. Write out the algorithm
#
# ERROR HANDLING:
#      Any Special Error handling to be noted.  Wager not less than 0. etc
#
# OTHER COMMENTS:
#      Any special comments
##
########################################################################
import turtle


class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):  # Sets the pen at the specified x, y coordinate
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):  # Draws a dot
        turtle.dot()


class Box(Point):

    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):  # Draws a box with the line color specified
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)


class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):  # Draws a box that gets filled with the specified color
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()


class Circle(Point):
    def __init__(self, x1, y1, radius,color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):  # Draws a circle with the line color of the specified color
        turtle.circle(self.radius)


class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fill_color):
        super().__init__(x1, y1, radius, color)
        self.fill_color = fill_color

    def draw_action(self):  # Draws a circle that gets filled with the chosen color
        turtle.fillcolor(self.fill_color)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()
