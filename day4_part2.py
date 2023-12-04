import re
import math

class Card:
    id = 0
    winning = {}
    myNumbers = {}
    copies = 1
    matches = 0

input = open("day4_puzzle.txt").readlines()
cards = []

for (i,value) in enumerate(input):
    numbers = re.findall(r"\d+", value)

    c = Card()
    c.ID = i
    c.winning = numbers[1:11]
    c.myNumbers = numbers[11:]
    c.matches = len([m for m in c.winning if m in c.myNumbers])
    
    cards.append(c)

for (i,c) in enumerate(cards):
    for j in range(c.matches):
        cards[i + j + 1].copies += c.copies
    
print(sum(c.copies for c in cards))