import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# #  what is the X and Y coordinate of locations:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("./us-states-game-start/50_states.csv")
all_states = data.state.to_list()

# if answer_state is one of the sates in all the states of the 50_states.csv
#   if it is right:
#       create a turtle write the name of the state at the state's x and y coordats:
guessed_sates = []

# while len(guessed_sates) < 50:
# answer_state = screen.textinput(title="guess the state", prompt="what's another state's name?")
# print(answer_state)
# if answer_state in all_states:
# t = turtle.Turtle()
# t.hideturtle()
# t.penup()
# state_date = data[data.state == answer_state]
# t.goto(int(state_date.x), int(state_date.y))
# series.item(): return the first element of the underlying as python scalar:
# t.write(state_date.state.item())


for guessed_states in range(0, 51):
    answer_state = screen.textinput(title=f"{len(guessed_sates)}/50 states correct",
                                    prompt="what's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
            # if state not in guessed_sates:
               # missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_sates.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date = data[data.state == answer_state]
        t.goto(int(state_date.x), int(state_date.y))
        # series.item(): return the first element of the underlying as python scalar:
        t.write(state_date.state.item())


