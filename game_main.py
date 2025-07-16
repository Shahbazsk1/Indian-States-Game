import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
img = "India-state.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("30_states.csv")
all_states = data.state.to_list()
guessed_state =[]


# this code is help to find x and y coordinate in img
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

while len(guessed_state) < 30:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/30 States Correct" ,
                                    prompt="What's another State's name? ").title()

    if answer_state == "Exit":
        # with list comprehension
        missing_state = [state for state in all_states if state not in guessed_state]
        # without list comprehension
        # missing_state = []
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

