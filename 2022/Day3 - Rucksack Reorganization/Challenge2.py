# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

letter_lc = 'abcdefghijklmnopqrstuvwxyz' #lowercase
letter_uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #uppercase

x = 1
letter_dict = {}

#Filling up the lowercase letter with their own values to dictionary 
for i in letter_lc:
    letter_dict[i] = x
    x += 1

#Filling up the uppercase letter with their own values to dictionary 
for i in letter_uc:
    letter_dict[i] = x
    x += 1

total_sum = 0

with open('input.txt', 'r') as f:
    text = f.readlines()

# To count till 3 for each group
counter = 0
group = {}
group[0] = {}
x = 0

# Fill up the groups per 3 rucksacks
for line in text:
    items = line.strip()
    group[x][counter] = items

    counter += 1
    if counter == 3: 
        counter = 0 # Reset counter
        x += 1
        group[x] = {}

group.pop(x) # Get rid of the last column since it is empty due to the previous code

total_sum = 0

for bags in group:
    bag_one = group[bags][0]
    bag_two = group[bags][1]
    bag_three = group[bags][2]

    letter = ''
    for item in bag_one:
        if item in bag_two and item in bag_three:
            letter = item
            break
    
    total_sum += (letter_dict[letter])

print(total_sum)