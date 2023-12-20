# 15 days to catch up on - I'm trying out GitHub Copilot to see if it makes me faster

data = open("day5_puzzle.txt").read().split("\n\n")

seeds = data[0].split(" ")[1:]
# convert seeds to an array of integers
seeds = [int(s) for s in seeds]

mapsto = {}
mappings = {}

for block in data[1:]:
    # extract X and Y from string "X-to-Y map:"
    lines = block.split("\n")
    x, t, y = lines[0].split(" ")[0].split("-")
    mapsto[x] = y
    mappings[x] = {}

    for l in lines[1:]:
        destination, source, length = l.split(" ")
        destination, source, length = (int(destination), int(source), int(length))

        for i in range(length):
            mappings[x][source + i] = destination + i

    
    print("Done")

finalvals = []
for s in seeds:
    x = "seed"

    soln = str(s)
    while x != "location":
        if s in mappings[x]:
            s = mappings[x][s]

        soln += "->" + str(s)

        x = mapsto[x]

    finalvals.append(s)
    
    print(soln)

print(min(finalvals))

    
    
