def main():
    print('rock,' ,'scissors',rock_paper_scissors('rock' ,'scissors'))
    print('scissors,', 'rock', rock_paper_scissors('scissors', 'rock'))
    print('rock,', 'paper', rock_paper_scissors('rock', 'paper'))
    print('paper,', 'rock', rock_paper_scissors('paper', 'rock'))
    print('paper,', 'scissors', rock_paper_scissors('paper', 'scissors'))
    print('scissors,', 'paper', rock_paper_scissors('scissors', 'paper'))
def rock_paper_scissors(player1,player2):
    """
    
    :param player1: Action of player1 
    :param player2: Actions of player2
    :return: who won
    """
    if player1 is 'rock' and player2 is 'scissors':
        return 1
    if player1 is 'scissors' and player2 is 'rock':
        return 2
    if player1 is 'scissors' and player2 is 'paper':
        return 1
    if player1 is 'rock' and player2 is 'paper':
        return 1
    if player1 is 'paper' and player2 is 'rock':
        return 2
    if player1 is 'paper' and player2 is 'scissors':
        return 2



main()
