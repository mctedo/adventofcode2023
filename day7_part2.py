import math

filename = "day7_puzzle.txt"
hands = []

def strength(s):
    strengths = 'AKQT98765432J'
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

    jokerCount = 0
    if 'J' in char_count:
        jokerCount = char_count['J']
        
    # remove key 'J' from char_count
    if 'J' in char_count:
        del char_count['J']

    if char_count == {}:
        max_char_count = 0
    else:
        max_char_count = max(char_count.values())

    # this was so painful to work out I had to pull it out
    def isFullHouse(char_count, max_char_count, jokerCount):
        if max_char_count == 3 and list(char_count.values()).count(2) == 1:
            return True
        elif list(char_count.values()).count(2) == 2 and jokerCount >= 1:
            return True
        elif max_char_count == 3 and jokerCount >= 1:
            return True
        else:
            return False        

    # test: 'A29J2'
    if max_char_count + jokerCount >= 5:
        fiveOfAKind.append(h)
    elif max_char_count + jokerCount == 4:
        fourOfAKind.append(h)
    elif isFullHouse(char_count, max_char_count, jokerCount):
        fullHouse.append(h)
    elif max_char_count + jokerCount == 3:
        threeOfAKind.append(h)
    elif list(char_count.values()).count(2) == 2 or (list(char_count.values()).count(2) == 1 and jokerCount >= 1):
        twoPair.append(h)
    elif list(char_count.values()).count(2) == 1 or (1 in char_count.values() and jokerCount >= 1):
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
