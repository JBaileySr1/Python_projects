import random

def play():
    user = input(" Choose: 'r' for rock, 'p' for paper, and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
        
    # r > s, s > p, and p > r
    if winner(user, computer):
        return 'You won!'

    return 'You lost!'

def winner(player_one, player_two):
    #return true if player_one wins
    # r > s, s > p, and p > r
    if (player_one == 'r' and player_two == 's') or (player_one == 's' and player_two == 'p') \
        or (player_one == 'p' and player_two == 'r'):
        return True

print(play())
