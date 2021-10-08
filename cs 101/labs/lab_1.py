#assigning the weights for later use
weight_labs = 0.7
weight_exams = 0.2
weight_attendance = 0.1

#asking for the all the grade inputs
print('**** Welcome to the LAB grade calculator! ****\n')
user_name = input('Who are we calculating grades for? ==> ')

grade_lab = int(input('\nEnter the Labs grade? ==> '))
if grade_lab > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    grade_lab = 100
elif grade_lab < 0:
    print('The lab value should have been zero or greater. It has been changed to zero')
    grade_lab = 0

grade_exams = int(input('\nEnter the EXAMS grade? ==> '))
if grade_exams > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    grade_exams = 100
elif grade_exams < 0:
    print('The exam value should have been zero or greater. It has been changed to zero')
    grade_exams = 0

grade_attendance = int(input('\nEnter the Attendance grade? ==> '))
if grade_attendance > 100:
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    grade_attendance = 100
elif grade_attendance < 0:
    print('The attendance value should have been zero or greater. It has been changed to zero')
    grade_attendance = 0

#getting the weighted grades
weight_labs *= grade_lab
weight_exams *= grade_exams
weight_attendance *= grade_attendance

weight_final = weight_labs + weight_exams + weight_attendance 

#printing grade info and testing to see what grade to output
print('\nThe weighted grade for {} is {:.1f}'.format(user_name, weight_final))
if weight_final >= 90 and weight_final <= 100:
    print('{} has a letter grade of A'.format(user_name))
elif weight_final >= 80 and weight_final < 90:
    print('{} has a letter grade of B'.format(user_name))
elif weight_final >= 70 and weight_final < 80:
    print('{} has a letter grade of C'.format(user_name))
elif weight_final >= 60 and weight_final < 70:
    print('{} has a letter grade of D'.format(user_name))
elif weight_final >= 0 and weight_final < 60:
    print('{} has a letter grade of F'.format(user_name))

#printing the exit statement
print('\n**** Thanks for useing the Lab grade calculator ****')
