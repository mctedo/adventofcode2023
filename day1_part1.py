import re

# Part 1
input = open("day1.txt").readlines()

total = 0

for i in input:
    num = re.findall(r'\d', i)
    first = num[0]
    last = num[-1]
    value = (int)(str(first) + str(last))
    total += value
    print("{} {} {}".format(first, last, value))

print("Part 1: {}".format(total))
