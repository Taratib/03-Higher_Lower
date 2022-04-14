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
    print('''For each game you will be asked to...
    - Enter a 'low' and 'high' number. The computer will randomly
    generate a 'secret' number between your two chosen numbers. it will use
    these numbers for all the rounds in a given game.
    - The computer will calculate how many guesses you are allowed
    - enter the number of rounds you want to play
    - guess the secret number

    Good luck !''')

    return ""


# Main Routine goes here
played_before = yes_no("Have you played the game before? ")
print()
if played_before == "no":
    instructions()

