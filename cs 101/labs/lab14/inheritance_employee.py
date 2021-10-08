
class Person(): #base, super #parent
       
       def __init__(self,fname,lname):
              self.fname = fname
              self.lname = lname
       def details(self):
              print('First name:',self.fname)
              print('Second name:',self.lname)
              self.more_details()
       def more_details(self):
              print(self.fname,'is a Person\n\n')

class Employee(Person): #child, derived

       def __init__(self, fname, lname, employee_id):
              super().__init__(fname, lname)
              self.employee_id = employee_id

       def more_details(self):
              print(self.fname,'is an Employee\n\n')

class HourlyEmployee(Employee):

       def __init__(self, fname, lname, employee_id, hours):
              super().__init__(fname, lname, employee_id)
              self.hours = hours

       def more_details(self):
              Employee.more_details(self)
              print(self.fname,' is an Hourly Employee\n\n')

if __name__ == '__main__':
       p1 = Person('Awais','Khan')
       e1 = Employee('Jon','Doe','1234')
       h1 = HourlyEmployee('Jane','Doe','1234','5')

       p1.details()
       e1.details()
       h1.details()


#Point (Base)
#Box ==> (Point)
#Boxfilled ==>(Box)
#Circle ==> (Point)
#Circlefilled ==>(Circle)

       
