import re

max = { 'red': 12, 'green': 13, 'blue': 14 }

input = open("day2_puzzle.txt").readlines()

totalValidGameIDs = 0

for g in input:
    id = (int)(re.search(r'Game (\d+)', g).group(1))
    valid = True

    # cubes
    drawn = g.split(': ')[1]
    sets = drawn.split(';')
    for s in sets:
        cubes = s.split(', ')
        for c in cubes:
            value = c.strip().split(' ')
            number = (int)(value[0])
            colour = value[1]

            if max[colour] < number:
                valid = False
                break
    
    if(valid): totalValidGameIDs += id

print("Valid Games: {}".format(totalValidGameIDs))

        


