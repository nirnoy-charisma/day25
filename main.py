import turtle as t
import pandas as pd
#displaying the screen
screen = t.Screen()
screen.title("USA State Game")
image = "blank_states_img.gif"
t.addshape(image)
t.shape(image)
#initializing
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guess_states = []
score = 0
#running the game until 50 is done
while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state name?").title()
#checking the answer and going to the position
    if answer_state in states:
        guess_states.append(answer_state)
        score += 1
        new_turtle = t.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        new_turtle.goto(x, y)
        new_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))
#exiting if u want
    elif answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guess_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
#lets u continue without clicking
    else:
        continue

t.mainloop()







