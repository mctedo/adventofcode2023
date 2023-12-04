import re
import math

cards = open("day4_puzzle.txt").readlines()

points = 0

for c in cards:
    splits = re.split(':|\|', c)
    winning = splits[1].strip().split(" ")
    mycards = splits[2].strip().split(" ")
    matches = len([c for c in mycards if c in winning and c != ''])
    if matches == 1: cardPoints = 1
    elif matches ==0: cardPoints = 0
    else: cardPoints = 1 * math.pow(2, matches-1)
    points += cardPoints


print("Points: {}".format(points))