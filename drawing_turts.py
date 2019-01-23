import turtle

def draw_sun():
    window = turtle.Screen()
    window.bgcolor("blue")
    square_parts = turtle.Turtle()
    square_parts.shape("circle")
    square_parts.shapesize(1,1,1)
    square_parts.speed(100)
    square_parts.color("orange")

    big_square = turtle.Turtle()
    big_square.shape("circle")
    big_square.shapesize(1,1,1)
    big_square.speed(100)
    big_square.color("yellow")

    core = turtle.Turtle()
    core.shape("circle")
    core.shapesize(1,1,1)
    core.speed(100)
    core.color("red")

    c = 0
    while c < 120:
        s = 0
        while s < 4:
            core.forward(62.5)
            core.right(90)
            square_parts.forward(125)
            square_parts.left(90)
            big_square.forward(250)
            big_square.right(90)
            s = s + 1
        core.left(3)
        square_parts.right(6)
        big_square.left(12)
        
        c = c + 1
        

    window.exitonclick()

draw_sun()
    
