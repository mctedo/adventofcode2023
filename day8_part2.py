input = open("day8_puzzle.txt").readlines()
instructions = input[0].strip()

# Extracting dictionary from list of strings
map = {item.split('=')[0].strip(): tuple(item.split('=')[1].strip()[1:-1].split(', ')) for item in input[2:]}

keys_with_a_as_last_character = [key for key in map.keys() if key.endswith('A')]

current_instructions = keys_with_a_as_last_character
current_index = 0
moves = 0


while not all(instruction.endswith('Z') for instruction in current_instructions):
    if instructions[current_index] == 'L':
        current_instructions = [map[instruction][0] for instruction in current_instructions]
    else:
        current_instructions = [map[instruction][1] for instruction in current_instructions]
    
    moves += 1
    current_index = (current_index + 1) % len(instructions)

print(moves)