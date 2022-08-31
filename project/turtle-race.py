from turtle import Turtle, Screen
import random

s = Screen()
s.setup(width=500, height=500)
user_input = s.textinput(title="Turtle Racing!!!", prompt="Which color will win Red or Green or Blue")





turtles = []

def create_turtles(color, w, h):
    t = Turtle()
    t.color(color)
    t.shape('turtle')
    t.penup()
    t.goto(w,h)
    t.speed(1)
    turtles.append(t)

def check_winner(turtle):

    if turtle.position()[0] >= 230:
        return True
    return False



def move_turtles():
    winner = ""
    while True:
        turtles[0].forward(random.choice([1,2,3]))
        if check_winner(turtles[0]):
            winner = "Red"
            print("Red is the winner")
            break
        turtles[1].forward(random.choice([1,2,3]))
        if check_winner(turtles[1]):
            winner = "Green"
            print("Green is the winner")
            break
        turtles[2].forward(random.choice([1,2,3]))
        if check_winner(turtles[2]):
            winner = "Blue"
            print("Blue is the winner")
            break

    if winner == user_input.upper():
        print('You won the bet')
    else:
        print('You lose the bet')



create_turtles('red',-230,-100)
create_turtles('green',-230,0)
create_turtles('blue',-230,100)

move_turtles()

s.exitonclick()

