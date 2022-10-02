import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")  # <--- this is a pandas DataFrame
states_correct = 0
guess_list = []
missed = []

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(-20, 270)
text.color("red")

is_guessing = True

while is_guessing:

    guess = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="What's another state's name?").title()
    state_column = states["state"].tolist()  # <--- a pandas Series, made into a List

    if guess in guess_list:
        text.clear()
        text.write(f"You've already guessed {guess}", align="center", font=("Courier", 16, "normal"))
        pass

    elif guess in state_column:
        text.clear()
        guess_list.append(guess)
        states_correct += 1

        current_row = states[states["state"] == guess]  # The entire row, DataFrame
        current_list = current_row.values.tolist()
        x = current_list[0][1]
        y = current_list[0][2]

        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.setpos(x, y)
        state.write(guess, align="center", font=("Courier", 8, "normal"))

    elif guess == "Exit":
        # When the user exists, we want to get a csv file with all the states we didn't guess
        # Bug - is doesn't always remove all the necessary states???
        # idk why...

        for elem in state_column:
            if elem in state_column and elem not in guess_list:
                missed.append(elem)

        states_df = pandas.DataFrame(missed)
        states_df.to_csv("missed_states.csv")
        break

    else:
        text.clear()
        text.write(f"{guess} is not a valid answer", align="center", font=("Courier", 16, "normal"))
