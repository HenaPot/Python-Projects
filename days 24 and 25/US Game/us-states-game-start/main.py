import turtle
import pandas

TEST_FONT = ("Arial", 15, "normal")
correct_guess = 0
correct_guesses_list = []

screen = turtle.Screen()
screen.title("U.S. Game")
screen.setup(height=600, width=750)

# setting up background to be the picture we choose
image = "blank_states_img.gif"
screen.addshape(image)
background = turtle.shape(image)

data = pandas.read_csv(filepath_or_buffer="50_states.csv")

game_is_on = True
while game_is_on:
    # setting up the title
    guess = screen.textinput(title=f"Guess the state {correct_guess}/50", prompt="What's another state's name?").title()

    # iterating over first column of the csv file --> accessing names of the states
    for state in data.state:
        if guess == state:
            correct_guess += 1
            correct_guesses_list.append(guess)

            # in case user guessed all the states it is game over
            if correct_guess == 50:
                game_is_on = False

                # show winning content
                win_turtle = turtle.Turtle(visible=False)
                win_turtle.penup()
                win_turtle.write("YOU GUESSED THEM ALL! GOOD JOB", align="center", font=("Arial", 25, "normal"))

            state_position = turtle.Turtle(visible=False)
            state_position.penup()

            # accessing data from the singular row from the csv file which corresponds to the guessed state
            singular_row = data[data.state == guess]

            # two ways of fetching the x and y coordinates from the csv file using pandas
            x_cor = int(singular_row[singular_row.columns[1]])
            y_cor = int(singular_row[singular_row.columns[2]])
            # alternatively just use .x and .y at the end of singular_row, shown below
            state_position.setposition(x=int(singular_row.x), y=int(singular_row.y))
            # state_position.write(f"{state}")
            state_position.write(f"{singular_row.state.item()}")

        # show end game content
        elif guess == "Exit":
            game_is_on = False
            score_turtle = turtle.Turtle(visible=False)
            score_turtle.penup()
            score_turtle.setposition(-80, 258)
            score_turtle.write(f"Your final score is {correct_guess}!", font=TEST_FONT)


turtle.mainloop()

