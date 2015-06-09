
from math import cos, sin, tan, pi, sqrt


import random
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    p = [.0987665432, .06793, sin(-1), cos(-1), -0.0000567, .08,]
    circle = 2 * pi + .0987654321
    triangle = random.triangular()
    l =  2 * random.choice(p) - 1
    w = cos(-1) * sin(1) + pi
    g = random.random() - cos(2) - sin(1)
    m  = -2 / 23
    z = cos(random.triangular())* sin(random.randint(1, 1))

    def another_expression(x, y):
        square = random.random() * x * -6 * y/3 % .123456789 - y / z % cos(0) - 2
        return sin(square*2 + l**2) % (cos(circle**-1/2 - z)) + random.randint(-1,1) % tan(triangle*1/2 - circle)

    return another_expression








    #def nuts_expression(x,y):
        #return (sin(-1) + cos(1))

    #def ultimate_function(x,y):

        #return tan(-1) - 1
    #return ultimate_function()


    #return crazy_expression

    #return expr
#expr = lambda x, y: (random.random() * 8**2) - 1

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
