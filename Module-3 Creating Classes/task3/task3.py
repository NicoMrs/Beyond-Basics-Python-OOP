## Classes can interact between each other 
# Object can be parsed as argument to class

class Online():
    
    def __init__(self, course, teacher):
        self.course = course
        self.teacher = teacher
        self.enrolled_students = []
        self.completed_students = []
     
        
    def enroll(self, student):
        """ take object student as argument"""
        if student.name in self.enrolled_students:
            print("!! {} already in list of enrolled students !!".format(student.name))
        else:
            self.enrolled_students.append(student)
            print('{} has been enrolled to the course!'.format(student.name))
        
    def get_course_details(self):
        print("{} is teaching {}.".format(self.teacher,self.course))
        
        print("Students enrolled are: < {} >.".format(', '.join(obj.name for obj in self.enrolled_students)))
        pass
        
    def average_grade(self,student):
        grades = student.grades
        print("Average grade is {} ".format(sum(grades)/len(grades)))
        
    def complete(self, student):
        
        if student.name in self.enrolled_students:
            self.completed_students.append(student.name)
            self.enrolled_students.remove(student.name)
        else:
            print('{} not in course'.format(student.name))
            pass
            
        

class Student():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades 
        
        
## Course creation
course = Online("OOP Python", "Josh")

        
        
## Student creation 
Names = ['Nicolas', 'Nathalie', 'Mickey']
Grades = [[10,10,8,9],
          [5,8,6,7],
          [4,4,8,8]
          ]
for i in range(len(Names)):
    name = Names[i]
    grades = Grades[i]
    
    # Student object creation
    student = Student(name, grades) ## list of object stored in Online class 
    
    # Append in course class
    course.enroll(student)

print()
course.get_course_details()
print()    
        
        
        
        