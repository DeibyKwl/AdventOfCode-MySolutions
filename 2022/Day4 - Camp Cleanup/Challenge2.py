#In how many assignment pairs do the ranges overlap?

with open('input.txt', 'r') as f:
    text = f.readlines()

total_sum = 0

for line in text:
    person1, person2 = line.split(',')
    
    person1_task = person1.split('-')
    person2_task = person2.split('-')
    
    if (int(person1_task[0]) <= int(person2_task[0]) and int(person1_task[1]) >= int(person2_task[0])):
        total_sum += 1
    elif (int(person2_task[0]) <= int(person1_task[0]) and int(person2_task[1]) >= int(person1_task[0])):
        total_sum += 1

print(total_sum)
