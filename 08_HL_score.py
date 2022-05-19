# RPS Component 6 - Soring System
game_summary = []
# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Results for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

# PLay Game
for item in test_results:
    rounds_played += 1

    # Generate computer choice

    result = item

    if result == "tie":
        result == "It's a tie"
        rounds_drawn += 1
    elif result == "loss":
        rounds_lost += 1


# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} ".format(rounds_won, rounds_lost, rounds_drawn))
print()

game_summary = input("Please press <Enter> to see your game summary / statistics...").lower()

print()
print("**** Game Scores *******")
for game in game_summary:
    print(game)

print()

# display game stats with $ values to the nearest whole number
print("******* Game Statistics ********")
print("Best: {} \nWorst: {} \nAverage: {}".format(rounds_won, rounds_lost, rounds_drawn))
