import turtle
import math

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
MAX_DISTANCE = math.ceil(math.sqrt(SCREEN_WIDTH ** 2 + SCREEN_HEIGHT ** 2) / 2)

TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target

PROJECTILE_SPEED = 1  # Projectile's animation speed

EAST = 0              # Angle of east direction
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
WEST = 180            # Angle of west direction

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.home()
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = int(input("Enter the projectile's angle 0-360: "))
distance = int(input(f'Enter the launch distance (1-{MAX_DISTANCE}): '))

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

xcor = turtle.xcor()
ycor = turtle.ycor()

# Did it hit the target?
is_in_x = ((xcor >= TARGET_LLEFT_X) and 
    (xcor <= (TARGET_LLEFT_X + TARGET_WIDTH)))
is_in_y = ((ycor >= TARGET_LLEFT_Y) and
    (ycor <= (TARGET_LLEFT_Y + TARGET_WIDTH)))
is_hit = is_in_x and is_in_y

# show message
if is_hit:
    print('Target hit!')
else:
    print('You missed the target.')

turtle.done()