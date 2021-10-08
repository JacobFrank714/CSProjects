import random


def play_again() -> bool:
    """ Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes """
    n = 0
    while n != -1:
        n = str.lower(input('Do you want to play again?'))
        if n == 'yes' or n == 'y':
            return True
        elif n == 'no' or n == 'n':
            return False
        else:
            print('You must enter Y/YES/N/NO to continue. Please try again')
            continue


def get_wager(bank: int) -> int:
    """ Asks the user for a wager chip amount.  Continues to ask if the result is <= 0 or greater than the amount they have """
    n = 0
    while n != -1:
        wager = int(input('Enter the amount to wager >> '))
        if bank >= wager > 0:
            return wager
        else:
            print('That wager is not possible. It must be more than 0 and less than or equal to your bank. try again')
            continue


def get_bank() -> int:
    """ Returns how many chips the user wants to play with.  Loops until a value greater than 0 """
    n = 0
    while n != -1:
        bank = int(input('Enter the amount for your pot'))
        if bank < 0:
            print('You must enter a positive number')
            continue
        else:
            return bank


def get_payout(wager, matches):
    """ Returns how much the payout is.. 3 times the wager if 3 matched, 2 times the wager if 2 match, 1 times the wager if 1 matched, and negative wager if 0 match """
    if matches == 3:
        return wager * 3
    elif matches == 2:
        return wager * 2
    elif matches == 1:
        return wager
    else:
        return wager * -1

def get_slot_results() -> tuple:
    """ Returns the result of the dice roll """
    diea = random.randint(1, 6)
    dieb = random.randint(1, 6)
    diec = random.randint(1, 6)
    dice = (diea, dieb, diec)
    return dice

def get_matches(diea, dieb, diec) -> int:
    """ Returns how many matches there are """
    n = -1
    while n == -1:
        i = 0
        if diea == user_guess:
            i += 1
        if dieb == user_guess:
            i += 1
        if diec == user_guess:
            i += 1
        return i
def get_guess() -> int:
    """ Gets user's guess for the dice roll """
    n = 0
    while n == 0:
        guess = int(input('Enter a number from (1 - 6) == > '))
        if 1< guess > 6:
            print('Your guess has to be between 1 and 6 or equal to 1 and 6')
            continue
        else:
            print()
            return guess

if __name__ == "__main__":
    playing = True
    while playing:
        print('welcome to Chuck-A-Luck\n')
        max_bank = 0
        bank = get_bank()
        starting_amount = bank
        i = 0
        while bank > 0:
            if bank > max_bank:
                max_bank = bank
            wager = get_wager(bank)
            user_guess = get_guess()

            die1, die2, die3 = get_slot_results()

            matches = get_matches(die1, die2, die3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your rolls were {} - {} - {}".format(die1, die2, die3))
            print("You matched", matches, "die")
            if matches == 0:
                print('You Lost!\n')
            elif matches > 0:
                print('You won {} dollars\n'.format(payout))
            print("You have {} dollars".format(bank))
            i += 1

        print("You lost all", starting_amount, "in", i, "rolls")
        print("The most chips you had was", max_bank)
        playing = play_again()