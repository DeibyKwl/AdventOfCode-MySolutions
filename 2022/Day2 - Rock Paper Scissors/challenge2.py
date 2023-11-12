# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
# A,B,C: Rock, Paper, Scissor
# X,Y,Z: lose, draw, win

total_sum = 0
text = ''
opponent_moves = {'A':1, 'B':2, 'C':3} # Only use for the draw

# Read the text file and save it into text variable
with open('input.txt', 'r') as f:
    text = f.readlines()
for line in text:
    opponent, player = line.split(' ')
    opponent, player = opponent.strip(), player.strip()

    # Tie
    if player == 'Y':
        total_sum += (3 + opponent_moves[str(opponent)])

    # Lose
    elif player == 'X':
        if opponent == 'A': # Rock
            total_sum += 3 # Scissor
        elif opponent == 'B': # Paper
            total_sum += 1 # Rock
        else: # Scissor
            total_sum += 2 # Paper

    # Win  
    else: 
        if opponent == 'A': # Rock
            total_sum += 8 # Paper
        elif opponent == 'B': # Paper
            total_sum += 9 # Scissor
        else: # Scissor
            total_sum += 7 # Rock

print(total_sum)