########################################################################
##
## CS 101
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
def output(filename, listcars):
    pass


def car_search(mpg, filename):
    cars = open(filename, 'r')
    cars = cars.readlines()
    result = []
    for line in range(len(cars)):

        if int(cars[line][8]) >= mpg:
            result.append(cars[line])
    return result


if __name__ == "__main__":
    while True:
        try:
            minMpg = int(input('Enter the minimum mpg ==> '))
            file_open = input('Enter the name of the input vehicle file ==> ')
            results = car_search(minMpg, file_open)
            outFileName = input('Enter the name of the file to output to ==> ')
            output(outFileName, results)
        except ValueError:
            print('You must enter a number for the fuel economy')
            continue
        except FileNotFoundError:
            print('Could not open file {}'.format(file_open))
            continue
        except IOError:
            print('There is an IO Error {}'.format(outFileName))
            continue

