from svg_turtle import SvgTurtle

t = SvgTurtle(1300, 1300)

iterations = 7
fractal_lenght = 1100


def curve():

    unit = "segment; t.left(60); segment; t.right(120); segment; t.left(60); segment"
    
    star = (unit+";t.right(120);")*3
    
    fractal = star
    for i in range(1,iterations):
        fractal = fractal.replace("segment", unit)
    fractal = fractal.replace("segment", "t.forward(fractal_lenght/3**iterations)")

    t.width(0)
    t.begin_fill()
    exec(fractal)
    t.end_fill()



def draw():
    t.penup()
    from math import sqrt
    t.setposition(-1*fractal_lenght/2, sqrt(3)*fractal_lenght/6)
    t.pendown()
    curve()

draw()
t.save_as("koch_star.svg")
