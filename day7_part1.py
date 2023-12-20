import math

filename = "day7_puzzle.txt"
hands = []

def strength(s):
    strengths = 'AKQJT98765432'
    index_concatenation = ''

    val = 0
    for i,char in enumerate(s[0]):
        val += strengths.index(char) * (math.pow(100,(len(s[0]) - i)))
        
    return val
    

with open(filename, 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(" ")
        string_value = parts[0]
        int_value = int(parts[1])
        hands.append((string_value, int_value))

print(hands)

fiveOfAKind = []
fourOfAKind = []
fullHouse = []
threeOfAKind = []
twoPair = []
onePair = []
highCard = []

for h in hands:

    char_count = {}

    for char in h[0]:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    if 5 in char_count.values():
        fiveOfAKind.append(h)
    elif 4 in char_count.values():
        fourOfAKind.append(h)
    elif 3 in char_count.values() and 2 in char_count.values():
        fullHouse.append(h)
    elif 3 in char_count.values():
        threeOfAKind.append(h)
    elif list(char_count.values()).count(2) == 2:
        twoPair.append(h)
    elif list(char_count.values()).count(2) == 1:
        onePair.append(h)
    else:
        highCard.append(h)

rank = []
rank.extend(sorted(highCard, key=strength, reverse=True))
rank.extend(sorted(onePair, key=strength, reverse=True))
rank.extend(sorted(twoPair, key=strength, reverse=True))
rank.extend(sorted(threeOfAKind, key=strength, reverse=True))
rank.extend(sorted(fullHouse, key=strength, reverse=True))
rank.extend(sorted(fourOfAKind, key=strength, reverse=True))
rank.extend(sorted(fiveOfAKind, key=strength, reverse=True))

winnings = 0
for i in range(len(rank)):
    winnings += (i+1) * rank[i][1]

print(winnings)