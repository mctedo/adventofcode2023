import re

input = open("day2_puzzle.txt").readlines()

totalPower = 0

for g in input:
    id = (int)(re.search(r'Game (\d+)', g).group(1))
    valid = True

    minReq = { 'red': 0, 'green': 0, 'blue': 0 }

    # cubes
    drawn = g.split(': ')[1]
    sets = drawn.split(';')
    for s in sets:
        cubes = s.split(', ')
        for c in cubes:
            value = c.strip().split(' ')
            number = (int)(value[0])
            colour = value[1]

            minReq[colour] = max(minReq[colour],number)

    power = minReq['red'] * minReq['green'] * minReq['blue']
    totalPower += power

print("Total Power: {}".format(totalPower))

        


