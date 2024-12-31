import turtle
import random
import pygame

def play_music(file):
    """Plays the specified MP3 file in the background."""
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.load(file)  # Load the MP3 file
    pygame.mixer.music.play(-1)  # Play the music on a loop (-1 means infinite loop)


def draw_stars(num_stars=100):
    """Draws random stars on a black background."""
    turtle.speed(9)
    turtle.hideturtle()
    turtle.penup()
    turtle.color("white")
    
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set plain black background

    screen_width = screen.window_width()
    screen_height = screen.window_height()

    for _ in range(num_stars):
        # Generate random coordinates within the screen
        x = random.randint(-screen_width // 2, screen_width // 2)
        y = random.randint(-screen_height // 2, screen_height // 2)
        # Generate random star size
        size = random.randint(1, 3)
        # Draw the star
        turtle.goto(x, y)
        turtle.dot(size)  # Use dot() for round stars

def draw_flower(x, y):
    # Set rose position
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(360)
    turtle.pendown()

    # Flower base
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.forward(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.forward(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.forward(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.forward(45)
    turtle.right(165)
    turtle.forward(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()

    # Petal 1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)

    # Petal 2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)

    # Leaves 1
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()
    turtle.right(135)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(85)
    turtle.left(90)
    turtle.forward(80)

    # Leaves 2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()
    turtle.left(135)
    turtle.forward(60)
    turtle.left(180)
    turtle.forward(60)
    turtle.right(90)
    turtle.circle(200, 60)

# Set up screen
turtle.speed(3)
turtle.bgcolor("black")  # Midnight blue background

# Play background music
play_music("Kal Ho Na Ho- Piano.mp3")

#Draw Stars
draw_stars(150)

# Draw roses
positions = [
    (-100, 100),  # Top-left
    (0, 100),     # Top-center
    (100, 100),   # Top-right
    (-70, 0),     # Bottom-left
    (30, 0),      # Bottom-center
    (130, 0)      # Bottom-right
]

for pos in positions:
    draw_flower(pos[0], pos[1])

turtle.done()

# Stop the music when the program is closed
pygame.mixer.music.stop()
