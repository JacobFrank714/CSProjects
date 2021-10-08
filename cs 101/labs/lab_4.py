print('Welcome to the Flarsheim Guesser!\n')

while True:#keeping the game in a loop until the user wants to stop
    print('Please think of a number between and including 1 and 100.')
    div_3 = 1    #to start my loops the variables need to be assigned
    div_5 = 1
    div_7 = 1
    ans = 'h'

    #checking to see if the remainder entered is possible for each input
    div_3 = int(input('What is the remainder when your number is divided by 3 ?'))
    while div_3 < 0 or div_3 > 3:
        if div_3 > 3:
            print('The value entered must be less than 3')
        elif div_3 < 0:
            print('The value entered must be 0 or greater')
        div_3 = int(input('What is the remainder when your number is divided by 3 ?'))

    div_5 = int(input('What is the remainder when your number is divided by 5 ?'))
    while div_5 < 0 or div_5 > 5:
        if div_5 > 5:
            print('The value entered must be less than 5')
        elif div_5 < 0:
            print('The value entered must be 0 or greater')
        div_5 = int(input('What is the remainder when your number is divided by 5 ?'))

    div_7 = int(input('What is the remainder when your number is divided by 7 ?'))
    while div_7 < 0 or div_7 > 7:
        if div_7 > 7:
            print('The value entered must be less than 7')
        elif div_7 < 0:
            print('The value entered must be 0 or greater')
        div_7 = int(input('What is the remainder when your number is divided by 7 ?'))
        
    for i in range(1, 101):
       if i %3 == div_3 and i %5 == div_5 and i %7 == div_7:    #checking to see what number match the users inputs
           print('your number is', i)
           
    while ans != 'Y' or ans !='y' or ans!= 'N' or ans!= 'n':    #trying to either restart or break the loop
        ans = input('Do you want ro play again? Y to continue, N to quit ==> ')
        if ans == 'Y' or ans == 'y':
            break
        elif ans == 'N' or ans == 'n':
            break
    if ans == 'N' or ans == 'n':
        break
    elif ans == 'Y' or ans == 'y':
        continue
            
