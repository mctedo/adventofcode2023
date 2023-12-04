import re
input = open("day3_puzzle.txt").read()
lines = input.split('\n')

symbols = { s: [] for s in input if s not in '0123456789.\n' }
symbolLocations = { (r,c): [] for r in range(140) for c in range(140) if lines[r][c] in symbols }

total = 0
for (i,line) in enumerate(lines):
    matches = re.finditer(r"\d+", line)
    coords = [(m.start(0), m.end(0),line[m.start(0):m.end(0)]) for m in matches]

    for (startsAt,endsAt,value) in coords:
        edges = {(r, c) for r in (i-1, i, i+1)
                       for c in range(startsAt-1, endsAt+1)}
        
        for o in edges:
            if o in symbolLocations:
                total += (int)(value)
                print("Matched {}".format(value))
                break

print(total)