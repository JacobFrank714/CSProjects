"""ALGORITHM :
        1. display the grade menu
        2. asks user to input what they want to do
            - if 1 then asks to input a number to add to the list of test scores
            - if 2 then asks to input a number to remove from the list of test scores
            - if 3 clears the list of test scores
            - if 4 then asks to input a number to add to the list of assignment scores
            - if 5 then asks to input a number to remove from the list of assignment scores
            - if 6 clears the list of assignment scores
            - if D then it displays the grade breakdown table
            - if Q then it quits the program"""
import math


def find_mean(lst):
    """calculates the average of the list that is past through"""
    try:
        mean = 0
        for n in lst:
            mean += n
        mean = mean / len(lst)
        return mean
    except ZeroDivisionError:
        return 0.00


def find_std(lst):
    """calculates the standard deviation of whatever list you pass through"""
    if len(lst) > 0:
        mean = find_mean(lst)
        total = 0
        for n in lst:
            total += (n - mean) ** 2
        std = total / len(lst)
        std = math.sqrt(std)
        return std
    else:
        return 'n/a'


def display_scores():
    """displays the grade break down chart"""
    if len(test) == 0 and len(assignments) != 0:
        print("{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}".format('type', '#', 'min', 'max', 'avg', 'std'))
        print("{:=<60}".format('='))
        print("{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}".format('Tests', len(test), 'n/a', 'n/a', 'n/a', 'n/a'))
        print("{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}".format('Programs', len(assignments), min(assignments),
                                                          max(assignments), find_mean(assignments),
                                                          find_std(assignments)))
    elif len(assignments) == 0 and len(test) != 0:
        print("{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}".format('type', '#', 'min', 'max', 'avg', 'std'))
        print("{:=<60}".format('='))
        print("{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}".format('Tests', len(test), min(test), max(test), find_mean(test),
                                                          find_std(test)))
        print("{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}".format('Programs', len(assignments), 'n/a', 'n/a', 'n/a', 'n/a'))
    elif len(test) == 0 and len(assignments) == 0:
        print("{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}".format('type', '#', 'min', 'max', 'avg', 'std'))
        print("{:=<60}".format('='))
        print("{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}".format('Tests', len(test), 'n/a', 'n/a', 'n/a', 'n/a'))
        print("{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}".format('Programs', len(assignments), 'n/a', 'n/a', 'n/a', 'n/a'))
    else:
        print('{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}'.format('type', '#', 'min', 'max', 'avg', 'std'))
        print('{:=<60}'.format('='))
        print('{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}'.format('Tests', len(test), min(test), max(test), find_mean(test),
                                                          find_std(test)))
        print('{:<19}{:<8}{:<10}{:<10}{:<10}{:<3}'.format('Programs', len(assignments), min(assignments),
                                                          max(assignments), find_mean(assignments),
                                                          find_std(assignments)))
    total_score = (0.4 * find_mean(assignments)) + (0.6 * find_mean(test))
    print('The wighted score is {:>11.2f}\n'.format(total_score))


if __name__ == "__main__":
    test = []
    assignments = []
    while True:
        try:
            choice = input('{:^33}\n'
                           '1 - Add Test\n'
                           '2 - Remove Test\n'
                           '3 - Clear Tests\n'
                           '4 - Add Assignment\n'
                           '5 - Remove Assignment\n'
                           '6 - Clear Assignments\n'
                           'D - Display Scores\n'
                           'Q - Quit\n'.format('Grade Menu'))
            if choice == '1':  # adds score to list of test scores
                try:
                    add = input('Enter the new Test score 0-100 ==> ')
                    if add < '0':
                        raise ValueError('Invalid Score: Enter a score higher than 0')
                    elif add.isalpha():
                        raise ValueError('Invalid Selection: must enter a number to add')
                    add = int(add)
                    test.append(add)
                except ValueError as ept:
                    print(ept)
            elif choice == '2':  # removes score from list of test scores
                try:
                    det = input('Enter the Test score to remove 0-100 ==> ')
                    if det < '0':
                        raise ValueError('Invalid Score: Enter a score higher than 0')
                    elif det.isalpha():
                        raise ValueError('Invalid Selection: must enter a number to remove')
                    det = int(det)
                    test.remove(det)
                except ValueError as ept:
                    print(ept)
            elif choice == '3':  # clears the test list
                test.clear()
            elif choice == '4':  # adds a score to assignments list
                try:
                    add = input('Enter the new Assignment score 0-100 ==> ')
                    if add < '0':
                        raise ValueError('Invalid Score: Enter a score higher than 0')
                    elif add.isalpha():
                        raise ValueError('Invalid Selection: must enter a number to add')
                    add = int(add)
                    assignments.append(add)
                except ValueError as ept:
                    print(ept)
            elif choice == '5':  # removes a score from the assignments list
                try:
                    det = input('Enter the Assignment score to remove 0-100 ==> ')
                    if det < '0':
                        raise ValueError('Invalid Score: Enter a score higher than 0')
                    elif det.isalpha():
                        raise ValueError('Invalid Selection: must enter a number to remove')
                    det = int(det)
                    assignments.remove(det)
                except ValueError as ept:
                    print(ept)
            elif choice == '6':  # clears assignments list
                assignments.clear()
            elif choice == 'd' or choice == 'D':  # displays the grade breakdown table
                display_scores()
            elif choice == 'q' or choice == 'Q':  # quits program
                break
            else:
                raise ValueError('Invalid selection: Try again')
        except ValueError as ept:
            print(ept)
