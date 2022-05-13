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


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def num_check(question, low, high):

    error= "Please enter an whole number between 1 and 10\n"

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

# Ask user for # of rounds...
print()
rounds = int_check("Please press <enter> for infinite mode "
                   "or the number of rounds you want.... ", 1, exit_code="")

if rounds == "":
    print("you chose infinite mode")
else:
    print("you asked for {} rounds".format(rounds))

# checks that response is an integer

low_num = int_check("Low Number: ")
print("You chose a low number of ", low_num)

# checks that response is an integer more than the low number
high_num = int_check("High Number: ", low_num)
print("You chose a high number of ", high_num)

# loop four times for easy testing
for item in range(0, 4):
    # checks that the response is either the exit code
    # or a number between low_num and high_num
    guess = int_check("Guess: ", low_num, high_num, "xxx")
    print("You guessed {}".format(guess))

# To Do
# set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

SECRET = 7
GUESSES_ALLOWED = 5

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int(input("Guess: "))  # replace this with function

    # check that guess is not duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again "
              "You *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < SECRET:
            print("Too low, try a higher number. Guess left: ")

        elif guess > SECRET:
            print("Too high, try a lower number. Guess left: ")
    else:
        if guess < SECRET:
            print("Too low!")
        elif guess > SECRET:
            print("Too high!")
