# HL components 5 - no duplicates

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


