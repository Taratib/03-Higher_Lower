import math

import random

# Functions go here


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")


def instructions():
    print("**** Welcome to the Higher Lower Game ****")
    print()
    print(''' For each game you will be asked to...
    - Enter a 'low' and 'high' number. The computer will randomly
      generate a 'secret' number between your two chosen numbers. it will use
      these numbers for all the rounds in a given game.
    - The computer will calculate how many
      guesses you are allowed
    - enter the number of rounds you want to play
    - guess the secret number

    Good luck !''')

    return ""


def check_rounds():
    while True:
        response = input("Rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def statement_generator(statement, decoration):

    sides = decoration * 0

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def num_check(question, low, high):

    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


def int_check(question, low=None, high=None, exit_code=None):
    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue

# Main routine goes here
played_before = yes_no("Have you played the game before? ")
print()
if played_before == "no":
    instructions()

game_summary = []

# ask user for # of rounds then loop...
rounds_played = 0
rounds_won = 0

# initialise lost / drawn counters
rounds_lost = 0
rounds_drawn = 0

# Ask user for # of rounds...
print()
rounds = int_check("Please press <enter> to begin.... ", 1, exit_code="")

if rounds == "":
    print("")
else:
    print("You asked for {} rounds".format(rounds))

# checks that response is an integer

low_num = int_check("Low Number: ")
high_num = int_check("High Number: ", low_num + 1)

var_range = high_num - low_num + 1
max_raw = math.log2(var_range)  # finds maximum # of guesses used
max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling)
max_guesses = max_upped + 1
print("Max Guesses: {}".format(max_guesses))

rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = statement_generator("Round {} of {} - You have {} guesses left ".format(rounds_played + 1, rounds,
                                                                                          max_guesses), "#")

    print(heading)
    choose_instruction = "Guess a number between {} and {}".format(low_num, high_num)
    rounds_played += 1

# To Do
# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

    secret = random.randint(low_num, high_num)
    guesses_allowed = (max_guesses)
    already_guessed = []
    guesses_left = guesses_allowed
    num_won = 0

    guess = ""

    while guess != secret and guesses_left >= 1:

        guess = int_check("Guess: ".format(low_num, high_num))  # replace this with function
        print()

        # check that guess is not duplicate
        if guess in already_guessed:
            statement_generator("You already guessed that number! Please try again "
                                "You *still* have {} guesses left".format(guesses_left), "!")
            print()
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guess == secret:
            statement_generator("Well done, you got it", "!")
            rounds_won += 1

        if guesses_left >= 1:

            if guess < secret:
                statement_generator("Too low, try a higher number. "
                                    "Guess left: {} ".format(guesses_left), "↑")
                print()
            elif guess > secret:
                statement_generator("Too high, try a lower number. "
                                    "Guesses left: {} ".format(guesses_left), "↓")
                print()
        else:
            decoration = "!"
            if guess < secret:
                feedback = "Too low!  You lose (ran out of guesses)"
            elif guess > secret:
                feedback = "Too high!  You lose (ran out of guesses)"
            rounds_lost += 1

    # end game if requested # of rounds has been played

    outcome = "Round {}: {}".format(rounds_played, secret)

    # Outputs results...
    game_summary.append(outcome)

    if rounds_played == rounds:
        break

rounds_won = rounds_played - rounds_lost

print()
statement_generator("Won: {} | Lost: {}".format(rounds_won, rounds_lost), "-")
print()

# Ask user if they want to see game summary

rounds = int_check("Please press <enter> to see your game summary.... ", 1, exit_code="")

# **** Calculate Game Stats ******

print()
print("**** Game History *******")
for game in game_summary:
    print(game)

print()

# display game stats with values to the nearest whole number
print("******* Game Statistics ********")
print("Worst: {} \nBest: {} ".format(rounds_won, rounds_lost))
