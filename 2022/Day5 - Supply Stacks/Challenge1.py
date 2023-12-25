# After the rearrangement procedure completes, what crate ends up on top of each stack?

with open('input.txt', 'r') as f:
    text = f.readlines()

i = 1
is_crate = True
crates = [[],[],[],[],[],[],[],[],[]]
instructions = []

for line in text:
    # Inserting crates to the arrays
    if is_crate:
        for crate in crates:
            if line[i] != ' ':
                crate.append(line[i])
            i += 4

        if '9' in crates[8]:
            is_crate = False
        
        i = 1 # reset
    
    # Store the instructions now
    else:
        steps = [int(i) for i in line.split() if i.isdigit()]
        instructions.append(steps)

# Get rid of first list since it is an empty line
instructions.pop(0)

from_index = 0
to_index = 0

for step in instructions:

    for from_crate in crates:
        if int(from_crate[len(from_crate) - 1]) == step[1]:
            from_index = int(from_crate[len(from_crate) - 1]) - 1
            break
    
    for to_crate in crates:
        if int(to_crate[len(to_crate) - 1]) == step[2]:
            to_index = int(to_crate[len(to_crate) - 1]) - 1
            break

    # Do the reordering of the crates
    for _ in range(step[0]):
        item = crates[from_index].pop(0)
        crates[to_index].insert(0,item)


# Print result
for item in crates:
    print(item[0],end='')