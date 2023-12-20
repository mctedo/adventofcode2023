import re
from functools import reduce
def extract_integers_from_string(string):
    integers = re.findall(r'\d+', string)
    return [int(num) for num in integers]

data = open("day6_puzzle.txt").readlines()
times = extract_integers_from_string(data[0])
distances = extract_integers_from_string(data[1])

wins = []
for i in range(len(times)):
    print(f"Time: {times[i]}, Distance: {distances[i]}")

    win = 0
    for j in range(times[i]):
        distance = (times[i] - j) * j
        if distance > distances[i]:
            win += 1

    wins.append(win)

# Multiply all values of wins together
result = reduce(lambda x, y: x * y, wins)
print("Result:", result)
    

