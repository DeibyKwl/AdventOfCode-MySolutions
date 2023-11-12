# What would your total score be if everything goes exactly according to your strategy guide?
# A,B,C: Rock, Paper, Scissor
# X,Y,Z: Rock, Paper, Scissor

total_sum = 0
text = ''
opponent_moves = ['A', 'B', 'C']
player_moves = {'X':1, 'Y':2, 'Z':3}

# Read the text file and save it into text variable
with open('input.txt', 'r') as f:
    text = f.readlines()
for line in text:
    opponent, player = line.split(' ')
    opponent, player = opponent.strip(), player.strip()

    # Tie
    if opponent_moves.index(opponent) == list(player_moves).index(player):
        total_sum += (3 + player_moves[str(player)])
        
    elif player == 'X': # Rock
        if opponent == 'B': #Paper
            total_sum += (0 + player_moves[str(player)])
        else: #Scissor
            total_sum += (6 + player_moves[str(player)])
            
    elif player == 'Y': # Paper
        if opponent == 'A': # Rock
            total_sum += (6 + player_moves[str(player)])
        else: # Scissor
            total_sum += (0 + player_moves[str(player)])

    elif player == 'Z': # Scissor 
        if opponent == 'B': # Paper
            total_sum += (6 + player_moves[str(player)])
        else: # Rock
            total_sum += (0 + player_moves[str(player)])

print(total_sum)
