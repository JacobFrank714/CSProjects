import random
def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
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
        
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if the result is <= 0 or greater than the amount they have '''
    n = 0
    while n != -1:
        wager = int(input('How much would you like to wager?'))
        if wager <= bank and wager > 0:
            return wager
        else:
            print('That wager is not possible. It must be more than 0 and less than or equal to your bank. try again')
            continue

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reela = random.randint(1, 10)
    reelb = random.randint(1, 10)
    reelc = random.randint(1, 10)
    reels = (reela, reelb, reelc)
    return reels

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc:
        return 3
    elif reela == reelb and reela != reelc or reela == reelc and reela != reelb or reelb == reelc and reelb != reela:
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    n = 0
    while n != -1:
        bank = int(input('How many chips would you like to play with?'))
        if bank > 101:
            print('That is too many. try again.')
            continue
        elif bank < 0:
            print('That is too few chips. try again.')
        else:
            return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 5 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager * 10 - wager
    elif matches == 2:
        return wager * 3 - wager
    else:
        return wager * -1    


if __name__ == "__main__":
    playing = True
    while playing:
        max_bank = 0
        bank = get_bank()
        starting_amount = bank
        i = 0
        while bank > 0:
            if bank > max_bank:
                max_bank = bank
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            i +=1

           
        print("You lost all", starting_amount, "in", i, "spins")
        print("The most chips you had was", max_bank)
        playing = play_again()
