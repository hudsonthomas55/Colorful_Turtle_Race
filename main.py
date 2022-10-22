from turtle import Turtle, Screen
import random

# Game setup and config
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


# Set up turtles
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Pop up window to request user place a bet on a turtle
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won the race!")
                screen.title((f"You won! The {winning_color} turtle won the race!"))
            else:
                print(f"You lose. The {winning_color} turtle won the race.")
                screen.title(f"You lose. The {winning_color} turtle won the race.")

        random_distance = random.randint(0,10)
        turtle.fd(random_distance)


screen.exitonclick()