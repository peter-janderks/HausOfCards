import matplotlib.pyplot as plt
import numpy as np

Results = {"Matthew": [3, 3, 2, 3, 2, 1, 1, 1, 4, 4, 4, 4, 3, 4, 4, 2, 2, 1, 2, 1, 3],
           "Henriette": [1, 2, 1, 3, 1, 2, 3, '_', 5, 5, 2, 1, 3, 3, 2, 3, 3, 4, 3, 2, 1],
           "Peter-Jan": [2, 1, 3, 1, '_', '_', '_', 2, 3, 2, 1, 3, 1, 2, '_', '_', '_', '_', 4, 3, 2],
           "Laurin": ['_', '_', '_', 2, 1, 3, '_', 4, 1, 6, 2, 2, 1, 1, '_', 1, 1, '_', '_', '_', '_'],
           "Janne": ['_', '_', '_', '_', '_', '_', 1, '_', '_', 4, '_', '_', '_', '_', '_', '_', '_', 3, '_', '_', '_'],
           "Ibbo": ['_', '_', '_', '_', '_', '_', 4, '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 2, 1, '_', 4],
           "Vinzent": ['_', '_', '_', '_', '_', '_', '_', 3, 2, 3, '_', '_', '_', '_', 1, '_', '_', '_', '_', '_', '_'],
           "Gabriella": ['_', '_', '_', '_', '_', '_', '_', '_', 1, 1, '_', '_', '_', '_', 3, '_', '_', '_', '_', '_', '_']}

print(len(Results['Matthew']))
players = list(Results.keys())
scores = dict()
for player in players:
    scores[player] = []

n_games = len(Results[players[0]])


def score_per_pos(n_players, player_pos):
    return(n_players - player_pos - 1)


for game in range(n_games-1):

    # calculate number of players
    n_players = 0
    for player in players:
        if type(Results[player][game]) == int:
            n_players += 1

    for player in players:
        position = Results[player][game]
        print(player)
        print(game, 'game')
        if type(position) == int:
            if game != 0:
                scores[player].append(score_per_pos(
                    n_players, Results[player][game]) + scores[player][game-1])
            else:

                scores[player].append(score_per_pos(
                    n_players, Results[player][game]))
        else:
            if game != 0:
                scores[player].append(scores[player][game-1])
            else:

                scores[player].append(0)

games = np.arange(n_games-1)
print(games, 'games')
fig = plt.figure()
for player in players:
    plt.plot(games, scores[player], label=player)

plt.legend(loc='upper left')
plt.show()
