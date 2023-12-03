
lines = open("day3_sample.txt").readlines()

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
            sumPartNumbers += number

print("Sum Part Numbers: {}".format(sumPartNumbers))

        

