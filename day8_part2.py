import math
input = open("day8_puzzle.txt").readlines()
instructions = input[0].strip()

# Extracting dictionary from list of strings
map = {item.split('=')[0].strip(): tuple(item.split('=')[1].strip()[1:-1].split(', ')) for item in input[2:]}

keys_with_a_as_last_character = [key for key in map.keys() if key.endswith('A')]

current_instructions = keys_with_a_as_last_character
current_index = 0
moves = 0
lcm = [None] * len(current_instructions)  # Initialize lcm list with None values

while not all(instruction.endswith('Z') for instruction in current_instructions) and None in lcm:
    if instructions[current_index] == 'L':
        current_instructions = [map[instruction][0] for instruction in current_instructions]
    else:
        current_instructions = [map[instruction][1] for instruction in current_instructions]
    
    moves += 1
    current_index = (current_index + 1) % len(instructions)

    for i, instruction in enumerate(current_instructions):
        if instruction.endswith('Z') and i < len(lcm) and lcm[i] is None:
            lcm[i] = moves
            if len(lcm) == len(current_instructions):  # Check if lcm list is complete
                break

    # FILEPATH: /C:/Users/micro/Documents/Dev/adventofcode2023/day8_part2.py
    
lcm_value = math.lcm(*lcm)
print(lcm_value)
    
    