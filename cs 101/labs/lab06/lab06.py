# import statements
import string

# functions


def character_value(n):
    for i in n:
        if i.isalpha():
            return string.ascii_uppercase.index(i)
        elif i.isdigit():
            return int(i)


def get_check_digit(n):
    global library_card
    k = 0
    library_digits = []
    while k <= 10:
        library_digits.append(character_value(n))
        k += 1
    check_digit_test = 0
    for i in range(0, len(library_card)-1):
        check_digit_test += ((i + 1) * library_digits[i])
    check_digit = check_digit_test % 10
    return check_digit


def verify_check_digit(i) -> tuple:
    check_digit = get_check_digit(i)
    if len(i) != 10:
        return False, 'The length of the number given must be 10'
    elif not i[0:5].isalpha():
        for n in range(len(i)):
            if i[n].isdigit():
                return False, 'The first 5 characters must be A-Z, the invalid is at {} is {}'.format(n, i[n])
    elif not i[7:9].isdigit():
        for n in range(7, len(i)):
            if i[n].isalpha():
                return False, 'The last 3 characters must be 0-9, the invalid character is at {} is {}'.format(n, i[n])
    elif not '1' <= i[5] <= '3':
        return False, 'The sixth character must be 1 2 or 3'
    elif not '1' <= i[6] <= '4':
        return False, 'The seventh character must be 1 2 3 or 4'
    elif check_digit != int(i[9]):
        return False, 'Check Digit {} does not match calculated value {}'.format(i[9], check_digit)
    else:
        return True, ''


def get_school(school_number):
    if school_number == '1':
        school = 'School of Computing and Engineering SCE'
        return school
    elif school_number == '2':
        school = 'School of Law'
        return school
    elif school_number == '3':
        school = 'College of arts and Sciences'
        return school
    else:
        return 'Invalid School'


def get_grade(grade_level):
    if grade_level == '1':
        grade = 'Freshman'
        return grade
    elif grade_level == '2':
        grade = 'Sophomore'
        return grade
    elif grade_level == '3':
        grade = 'Junior'
        return grade
    elif grade_level == '4':
        grade = 'Senior'
        return grade
    else:
        return 'Invalid Grade'


if __name__ == "__main__":

    # main program
    print("{:^60}".format('Linda Hall'))
    print('{:^60}'.format('Library Card Check'))
    print('=' * 60)
    while True:
        library_card = input('Enter Library card. Hit Enter to Exit ==> ')
        b_check, error_msg = verify_check_digit(library_card)
        if not b_check:
            print('Library card is invalid')
            print(error_msg)
            continue
        else:
            print('Library card is valid.')
            print('The card belongs to a student in {}'.format(get_school(library_card[5])))
            print('The card belongs to a {}'.format(get_grade(library_card[6])))
            continue
