file_path = "day9_puzzle.txt"

history = []
with open(file_path, 'r') as file:
    lines = file.readlines()
    lines = [[int(value) for value in line.strip().split(' ')] for line in lines]

for line in lines:
    h = [line]
    history.append(h)

for h in history:
    while any(v != 0 for v in h[-1]):
        differences = [h[-1][i + 1] - h[-1][i] for i in range(len(h[-1])-1)]
        h.append(differences)
    
    i = len(h) - 2
    while i >= 0:
        new_value = h[i+1][-1] + h[i][-1]
        h[i].append(new_value)
        i -= 1

# Sum the final value of each list in history
sum_of_final_values = [h[0][-1] for h in history]

print(sum(sum_of_final_values))