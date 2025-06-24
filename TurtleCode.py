import turtle
import time
from datetime import datetime

# Setup screen
screen = turtle.Screen()
screen.title("Turtle Clock")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Create turtle for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(3)


def draw_clock_face():
    pen.penup()
    pen.goto(0, -250)
    pen.pendown()
    pen.circle(250)

    # Draw hour markers
    pen.penup()
    for hour in range(12):
        angle = 30 * hour
        pen.goto(0, 0)
        pen.setheading(90 - angle)
        pen.forward(200)
        pen.pendown()
        pen.forward(50)
        pen.penup()

def draw_hand(length, angle, color):
    pen.penup()
    pen.goto(0, 0)
    pen.color(color)
    pen.setheading(90 - angle)
    pen.pendown()
    pen.forward(length)
    pen.penup()

def draw_clock():
    pen.clear()
    draw_clock_face()

    now = datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second

    # Calculate angles
    hour_angle = (hours + minutes / 60) * 30
    minute_angle = minutes * 6
    second_angle = seconds * 6

    draw_hand(100, hour_angle, "black")
    draw_hand(150, minute_angle, "blue")
    draw_hand(180, second_angle, "red")

# Update every second
while True:
    pen.reset()
    pen.speed(0)
    pen.hideturtle()
    pen.pensize(3)
    draw_clock()
    screen.update()
    time.sleep(1)