game_summary = []

rounds_lost = 0
rounds_played = 5

for item in range (1, 6):
    result = input("choose result: ")

    outcome = "Round {}: {}".format(item, result)

    if result == "lost":
        rounds_lost += 1

    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost

# **** Calculate Game Stats ******

print()
print("**** Game History *******")
for game in game_summary:
    print(game)

print()

# display game stats with $ values to the nearest whole number
print("******* Game Statistics ********")
print("Win: {} \nLose: {}".format(rounds_won, rounds_lost))