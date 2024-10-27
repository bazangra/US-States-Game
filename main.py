import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
list = data.state.to_list()

guessed_states = []
title1 = "Guess The State"
score = 0

is_on = True
while is_on:
    answer_state = screen.textinput(title=title1, prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in list:
        guessed_states.append(answer_state)
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(answer_state)
        score += 1
        title1 = f"{score}/50 States Correct"
    if score > 49:
        is_on = False

missing_states = [state for state in list if state not in guessed_states]
data = pandas.DataFrame(missing_states)
data.to_csv("missed.csv")

screen.exitonclick()