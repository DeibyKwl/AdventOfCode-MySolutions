# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

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

for line in text:
    items = line.strip()

    # Splitting the items in two compartments
    first_comp = items[0:int(len(items) / 2)]
    second_comp = items[int(len(items) / 2):]

    letter = ''
    for item in first_comp:
        if item in second_comp:
            letter = item
            break
    
    total_sum += letter_dict[letter]

print(total_sum)
   