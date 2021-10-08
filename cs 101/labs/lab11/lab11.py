'''Algorithm:
        1. opens and reads the friends.txt file
        2. makes a dictionary of every user's list of friends
        3. asks user what they want to know
        4. a. if they input I it asks them to input two names and the output is the friends they share
           b. if they input D, it asks them to input two names and the output is the friends that the first person has that the second person doesn't
           c. if they input S, it asks them to input two names and the output is the friends that they don't share
           d. if they input Q, it quits the program'''


def read_file():  # opens the friends file and makes a dict of the users with a value of a set of their friends
    people = {}
    user, friend = [], []  # for storage for later use
    file = open('friends.txt', 'r')
    for line in file:  # splits the line into a list of strings
        line = line.upper().strip("\n").split(" ")
        user.append(line[0])
        friend.append(line[1])

    for i, friend in enumerate(friend):
        if user[i] in people:
            people[user[i]].add(friend)  # adds a new person to a user's set of friends
        else:
            people[user[i]] = {friend}  # adds a new user with that one friend in the set
    file.close()
    return people


def shared(dic):
    while True:
        try:
            n1 = input('Enter a valid person ==> ').upper()  # gets the first set of friends
            if n1 not in dic.keys():
                raise KeyError
            n2 = input('Enter a valid person ==> ').upper()  # gets the second set of friends
            if n2 not in dic.keys():
                raise IndexError

            shared_friends = dic[n1].intersection(dic[n2])
            return shared_friends
        except KeyError:
            print(n1, 'is not part of this network, enter another name')
        except IndexError:
            print(n2, 'is not part of this network, enter another name')


def just_n1(dic):
    while True:
        try:
            n1 = input('Enter a valid person ==> ').upper()  # gets the first set of friends
            if n1 not in dic.keys():
                raise KeyError
            n2 = input('Enter a valid person ==> ').upper()  # gets the second set of friends
            if n2 not in dic.keys():
                raise IndexError

            n1_friends = dic[n1].difference(dic[n2])
            return n1_friends
        except KeyError:
            print(n1, 'is not part of this network, enter another name')
        except IndexError:
            print(n2, 'is not part of this network, enter another name')


def not_shared(dic):
    while True:
        try:
            n1 = input('Enter a valid person ==> ').upper()  # gets first set of friends
            if n1 not in dic.keys():
                raise KeyError
            n2 = input('Enter a valid person ==> ').upper()  # gets second set of friends
            if n2 not in dic.keys():
                raise IndexError

            not_shared_friends = dic[n1].symmetric_difference(dic[n2])
            return not_shared_friends
        except KeyError:
            print(n1, 'is not part of this network, enter another name')
        except IndexError:
            print(n2, 'is not part of this network, enter another name')


if __name__ == '__main__':
    while True:
        user_friends = read_file()
        print('Social Network\n')  # used as the main menu for the program
        action = input('I. Find all friends shared by 2 people\n'
                       'D. Find all friends of X, That person Y does not have\n'
                       'S. Find all friends that X and Y have, but do not share with each other\n'
                       'Q. Quit\n\n'
                       '==>').upper()
        if action == 'I':
            print(shared(user_friends))

        elif action == 'D':
            print(just_n1(user_friends))

        elif action == 'S':
            print(not_shared(user_friends))

        elif action == 'Q':
            break
