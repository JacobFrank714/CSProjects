''' Algorythm:
    1.Ask user for the name of the file they wish to read the grades from
    2.program searches the file for for the given file name
    3.if the file name is found the program reads the file and makes the information into a list of lists containing the information of each row in it's own list
    4.if the file name is not found it will tell the user that the file could not be found and ask the user to input a new name
    5.once the files information is recorded it is used to calculated all of the grade percentages
    6.once the calculations are done then a list is made for each student that contains all the grade information for the student
    7.all the lists are then combined into a list of the students information
    8.the list of the lists is then writen to the report file writing each list in it's own line in the file
    9.then the report file is closed and the program asks the user for a new file name until the user inputs quit
    10.once the user inputs quit the program ends'''


import csv


def read_in_file(file_name):
    """Makes a list of lists of each row in the csv file"""
    file = open(file_name)
    contents = csv.reader(file)
    contents = list(contents)
    file.close()
    return contents


def grade_calculations(grade_list):
    students_grades = []
    for i in grade_list:
        name = i[0]
        exam1 = int(i[1])
        exam2 = int(i[2])
        ass1 = int(i[3])
        ass2 = int(i[4])
        exam1_p = exam1 * 0.1
        exam2_p = exam2 * 0.1
        ass1_p = ass1 * 0.05
        ass2_p = ass2 * 0.05
        total_p = exam1_p + exam2_p + ass1_p + ass2_p
        grade = (total_p / 30) * 100
        if grade >= 91:
            letter_grade = 'A'
        elif 90 >= grade >= 81:
            letter_grade = 'B'
        elif 80 >= grade >= 71:
            letter_grade = 'C'
        elif 70 >= grade >= 61:
            letter_grade = 'D'
        elif 60 >= grade:
            letter_grade = 'F'
        student_info = [name, exam1, exam2, ass1, ass2, exam1_p, exam2_p, ass1_p, ass2_p, total_p, grade, letter_grade]
        students_grades.append(student_info)
    return students_grades


def open_write_file(grade_files):
    with open('mid_report.csv', 'w') as csvfile:
        grade_writer = csv.writer(csvfile)
        grades = grade_calculations(grade_files)
        for i in range(len(grades)):
            grade_writer.writerow(grades[i])


if __name__ == '__main__':
    while True:
        try:
            student_grades = input('Enter the name of the file (quit to exit) ==> ')
            if student_grades.lower() == 'quit':
                break
            grade_file = read_in_file(student_grades)
            print('Reading data and outputting to mid_report.csv...')
            open_write_file(grade_file)
        except FileNotFoundError:
            print('Could not open the file, please enter another.')
            continue
