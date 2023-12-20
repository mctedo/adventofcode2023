input = open("day8_puzzle.txt").readlines()
instructions = input[0].strip()

# Extracting dictionary from list of strings
map = {item.split('=')[0].strip(): tuple(item.split('=')[1].strip()[1:-1].split(', ')) for item in input[2:]}

current_instruction = 'AAA'
current_index = 0
moves = 0

while current_instruction != 'ZZZ':
    if instructions[current_index] == 'L':
        current_instruction = map[current_instruction][0]
    else:
        current_instruction = map[current_instruction][1]
    
    moves += 1
    current_index = (current_index + 1) % len(instructions)

print(moves)