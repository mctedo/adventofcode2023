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
    mappings[x] = []

    for l in lines[1:]:
        destination, source, length = l.split(" ")
        mappings[x].append((int(destination), int(source), int(length)))
    
    print("Done")

finalvals = []
for z in range(len(seeds)):
    if z % 2 != 0:
        continue

    for s in range(seeds[z], seeds[z] + seeds[z+1]):
        x = "seed"

        soln = str(s)
        while x != "location":
            for (destination,source,length) in mappings[x]:
                if s in range(source, source+length):
                    s = s - source + destination
                    break

            soln += "->" + str(s)

            x = mapsto[x]

        finalvals.append(s)
        
        print(soln)

print(min(finalvals))

    
    
