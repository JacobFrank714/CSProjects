import random


def shuffle(p_1, p_2, p_3):
    """Shuffles the hand of all of the player"""
    random.shuffle(p_1)
    random.shuffle(p_2)
    random.shuffle(p_3)


def take_card(card, player_thief, player_stolen):
    """When a player takes another players card"""
    while 0 >= card or card > 3:
        card = int(input('Invalid selection\n'
                         'Choice a different card: '))
        continue

    n = player_stolen.pop(card - 1)
    player_thief.append(n)


def ai_turn():
    """Generates a random number for the ai to use to take their turn"""
    n = random.randint(1, 3)
    return n


def check_list(lst):
    """checks after every turn if a player wins"""
    ele = lst[0]
    chk = True

    # Comparing each element with first item
    for item in lst:
        if ele != item:
            chk = False
            break
    return chk


if __name__ == "__main__":

    while True:
        i = 1
        x1 = [1, 2, 3]
        x2 = [1, 2, 3]
        x3 = [1, 2, 3]
        shuffle(x1, x2, x3)
        # noinspection PyStringFormat
        print('Welcome to Shuffle Cards:\n'
              'Number of players is 3 and total cards for each player are 3\n'
              'Lets shuffle the cards\n'
              'we have 2 AI players and 1 Human player\n'
              'Player 1 AI Cards: {}\n'
              'Player 2 AI Cards: {}\n'
              'Player 3 Human Cards: {}\n'.format(x1, x2, x3))
        while True:
            x1 = x1
            x2 = x2
            x3 = x3
            print('{:=<50}\n'
                  'Round :  {}\n'
                  '{:=<50}\n'.format('', i, ''))
            x = ai_turn()
            take_card(x, x1, x2)
            print('AI_1 decision is : {}\n'
                  'player1 cards: {}\n'
                  'player2 cards: {}\n'
                  'Human cards: {}\n'.format(x, x1, x2, x3))
            x = ai_turn()
            take_card(x, x2, x3)
            print('AI_2 decision is : {}\n'
                  'player1 cards: {}\n'
                  'player2 cards: {}\n'
                  'Human cards: {}\n'.format(x, x1, x2, x3))
            choice = int(input('Enter 1 for card 1\n'
                               'Enter 2 for card 2\n'
                               'Enter 3 for card 3\n'
                               'Enter your choice: '))
            take_card(choice, x3, x1)
            print('player1 cards: {}\n'
                  'player2 cards: {}\n'
                  'Human cards: {}\n'.format(x1, x2, x3))
            i += 1
            if check_list(x1):
                print('AI_1 WON!!\n'
                      'Thanks for playing')
                break
            elif check_list(x2):
                print('AI_2 WON!!\n'
                      'Thanks for playing')
                break
            elif check_list(x3):
                print('You WON!!\n'
                      'Thanks for playing')
                break
            else:
                continue
        play_again = input('Do you want to play again: Y/N\n').lower()
        if play_again == 'y':
            continue
        elif play_again == 'n':
            break
