# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

# Personal note: I never use the lines that had 'dir' in it. I also did not take the command 'ls' into account, I just skip it.

with open('input.txt', 'r') as f:
    text = f.readlines()

total_space = 70000000
required_space = 30000000
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

outermost_dir_size = 0

# Add the rest of the directories 
for dir in dir_parent:
    dir_list.append(dir)
    if dir[0] == '/':
        outermost_dir_size = dir[1]

# Find the size of space we must delete
free_up_size = required_space - (total_space - outermost_dir_size)

smallest_size_required = total_space
for dir in dir_list:
    if dir[1] >= free_up_size and dir[1] < smallest_size_required:
        smallest_size_required = dir[1]

print(smallest_size_required)