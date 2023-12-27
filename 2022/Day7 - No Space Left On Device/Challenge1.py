# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

# Personal note: I never use the lines that had 'dir' in it. I also did not take the command 'ls' into account, I just skip it.

with open('input.txt', 'r') as f:
    text = f.readlines()

LIMIT = 100000
ls_mode = False
dir_parent = []
dir_list = []

for line in text:

    if '$ cd' in line:
        line = line.split()
        if line[2] != '..':
            new_file = [line[2], 0]
            dir_parent.append(new_file)
            
        # When leaving directory, append it to the list, assuming we will never
        # go back to this directory.
        else:
            dir_list.append(dir_parent[-1]) 
            del dir_parent[-1]
       
    elif '$' not in line:
        line = line.split()
        if 'dir' not in line:
            for parent in dir_parent:
                parent[1] += int(line[0])

# Add the rest of the directories 
for dir in dir_parent:
    dir_list.append(dir)

# Sum of all directories sizes which are at most 100000
total_sizes = 0

for dir_sizes in dir_list:
    if dir_sizes[1] <= LIMIT:
        total_sizes += dir_sizes[1]

print(total_sizes)