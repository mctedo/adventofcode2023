
input = open("day3_sample.txt").read()
lines = input.split('\\n')

symbols = { s: [] for s in input if s not in '0123456789.\n' }
symbolLocations = { (r,c): [] for r in range(len(lines[0])) for c in range(len(lines)) if input[r][c] in symbols }

sumPartNumbers = 0

for l in range(len(lines)):

    i = 0
    while i < len(lines[l]):
        # Number?
        strNumber = ''
        startsAt = i
        while lines[l][i].isnumeric():
            strNumber += lines[l][i]
            i += 1

        endsAt = i
        i += 1

        if strNumber != '':
            number = (int)(strNumber)
            print(number)

            # Now check if the number is surrounded by any symbol
            valid = False

            edge = {(r, c) for r in (l-1, l, l+1)
                       for c in range(startsAt-1, endsAt+1)}
            
            for o in edge:
                if o in symbolLocations:
                    sumPartNumbers += number
                    print("Matched {}".format(number))
                    break

print("Sum Part Numbers: {}".format(sumPartNumbers))

        

