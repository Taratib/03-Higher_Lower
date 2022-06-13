# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
# Results for testing purposes
test_results = ["won", "won", "loss", "loss",]

# PLay Game
for item in test_results:
    rounds_played += 1
    # Generate computer choice
    result = item

    if result  == "loss":
        rounds_lost += 1

# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost

# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {}".format(rounds_won, rounds_lost))
print()
print("Thanks for playing")