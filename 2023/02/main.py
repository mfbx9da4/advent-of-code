import os
dir_path = os.path.dirname(os.path.realpath(__file__))


max_reds = 12
max_greens = 13
max_blues = 14

sum_games = 0
power_set_sum = 0
with open(dir_path + '/input.txt', 'r') as f:
  gameId = 1
  for game in f.readlines():
    rounds = game.split(':')[1]
    ok = True
    reds = 0
    greens = 0
    blues = 0
    for round in rounds.split(';'):
      for item in round.split(','):
        count, color = item.strip().split(' ')
        if color == 'red': reds = max(reds, int(count))
        if color == 'green': greens = max(greens, int(count))
        if color == 'blue': blues = max(blues, int(count))
        if color == 'red' and int(count) > max_reds:
          ok = False
        elif color == 'green' and int(count) > max_greens:
          ok = False
        elif color == 'blue' and int(count) > max_blues:
          ok = False
    if ok:
      sum_games += gameId
    power_set_sum += reds * greens * blues
    gameId += 1
print(sum_games)
print(power_set_sum)