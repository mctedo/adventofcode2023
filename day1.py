import re

# Part 2

input = open("day1.txt").readlines()

total = 0
search = { '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }

for i in input:
    firstNoAt = 1000
    firstNo = -1
    lastNoAt = -1
    lastNo = -1

    for key in search:
        index = i.find(key)
        if index > -1 and index < firstNoAt:
            firstNo = search[key]
            firstNoAt = index
        
        rindex = i.rfind(key)
        if rindex >-1 and rindex > lastNoAt:
            lastNo = search[key]
            lastNoAt = rindex

    value = (int)(str(firstNo) + str(lastNo))
    total += value
    print("{} {} {}".format(firstNo, lastNo, value))
            
print("Part 2: {}".format(total))