# Main routine more efficent than v2
import math
# Checks for the a number that is more then zero


def check_rounds():
    while True:
        print()
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

rounds_played = 0

# Ask user for # of rounds, <enter> for infinite mode

low_num = int(input("Low: "))  # use int check in due course
high_num = int(input("High: "))  # use int check in due course

var_range = high_num - low_num + 1
max_raw = math.log2(var_range)  # finds maximum # of guesses used
max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling)
max_guesses = max_upped + 1
print("Max Guesses: {}".format(max_guesses))


rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of the Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {} - You have {} guesses left ".format(rounds_played + 1, rounds, max_guesses)

    print(heading)

    rounds_played += 1

    # **** rest of loop / game *****
    SECRET = 7
    GUESSES_ALLOWED = (max_guesses)

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

            # end game if requested # of rounds has been played
            if rounds_played == rounds:
                break

# Put end game content here
print("Thank you for playing")