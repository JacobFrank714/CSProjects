''' Algorithm:
       1.Ask user for the file name
       2.Ask user for an offense
       3.print a table showing how many occurrences of that offense happened in each zip code'''
# imports
import csv


# functions
def month_from_number(numb):
    """Converts an integer from 1 - 12 into a month"""
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    if numb <= 0 or numb > 12:
        raise ValueError('Month must be 1-12')
    return months[numb]


def read_in_file(file_name):
    """Makes a list of lists of each row in the csv file"""
    file = open(file_name, encoding="utf-8")
    contents = csv.reader(file)
    contents = list(contents)
    file.close()
    return contents


def create_reported_date_dict(lst):
    """Returns a dictionary of dates and how many times a crime happened on that date"""
    report = {}
    lst1 = []
    lst.remove(lst[0])
    for i in range(len(lst)):
        lst1.append(lst[i][1])
    for key in lst1:
        if key in report:
            report[key] = report[key] + 1
        else:
            report[key] = 1
    return report


def create_reported_month_dict(lst):
    """Returns a dictionary that has how many offenses happened in a given month"""
    lst.remove(lst[0])
    lst1 = []
    lst2 = []
    report_month = {}
    for i in range(len(lst)):
        lst1.append(lst[i][1])
    for i in lst1:
        lst3 = i.split('/')
        lst2.append(int(lst3[0]))
    for key in lst2:
        if key in report_month:
            report_month[key] = report_month[key] + 1
        else:
            report_month[key] = 1
    return report_month


def create_offense_dict(lst):
    """Returns a dictionary that has the number of times an offense occurs"""
    report_offense = {}
    lst1 = []
    lst.remove(lst[0])
    for i in range(len(lst)):
        lst1.append(lst[i][7])
    for key in lst1:
        if key in report_offense:
            report_offense[key] = report_offense[key] + 1
        else:
            report_offense[key] = 1
    return report_offense


def create_offense_by_zip(lst):
    """Returns a dictionary that has an offense and how many times the offense happened in each zip code"""
    report_offense_zip = {}
    lst1 = []
    lst.remove(lst[0])
    for i in range(len(lst)):
        lst1.append((lst[i][7], lst[i][13]))
    for i in lst1:
        if i[0] in report_offense_zip:
            if i[1] in report_offense_zip[i[0]]:
                report_offense_zip[i[0]] = report_offense_zip[i[0]][i[1]] + 1
            else:
                report_offense_zip[i[0]][i[1]] = 1
        else:
            report_offense_zip[i[0]] = {i[1]: 1}
    return report_offense_zip


def find_max_number_offenses(dict):
    """finds the highest offenses in a month and offense with highest amount of occurrences"""
    dict_sorted = sorted(dict.items())
    max_offenses = 0
    max_month = 0
    for i in dict_sorted:
        if i[1] > max_offenses:
            max_offenses = i[1]
            max_month = i[0]
    return max_month, max_offenses


if __name__ == "__main__":
    # Main program
    while True:
        try:
            file_name = input('Enter the name of the date file ==>')
            file_contents = read_in_file(file_name)
            month, offenses = find_max_number_offenses(create_reported_month_dict(file_contents))
            offense, num_offenses = find_max_number_offenses(create_offense_dict(file_contents))
            print('The month with the highest # of crimes was {} with {} offenses'.format(month_from_number(month),
                                                                                          offenses))
            print('The offense with the highest # of crimes is {} with {} offenses'.format(offense, num_offenses))
            break
        except FileNotFoundError:
            print('Could not find the file specified.', file_name, 'not found')
            continue
    while True:
        try:
            offense_by_zip = create_offense_by_zip(file_contents)
            offense = input('Enter an offense ')
            if not offense_by_zip[offense]:
                raise ValueError
            print('{} offenses by Zip Code\n'
                  '{:<15} {:>15}\n'
                  '{:<30}'.format(offense, 'Zip Code', '# Offenses', '='*31))
            for offense in offense_by_zip[offense]:
                for k in offense:
                    print('{:<15} {:>15}'.format(k, 'v'))
            break
        except KeyError:
            print('Not a valid offense found, please try again')
            continue
