# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:24:19 2023

@author: Nico
"""

class Online():
    
    def __init__(self, course, teacher):
        self.course = course
        self.teacher = teacher
        self.enrolled_students = []
        self.completed_students = []
        
    def enroll(self, student_name):
        if student_name in self.enrolled_students:
            print("!! {} already in list of enrolled students !!".format(student_name))
        else:
            self.enrolled_students.append(student_name)
            print('{} has been enrolled to the course!'.format(student_name))
        
    def get_course_details(self):
        print("{} is teaching {}.".format(self.teacher,
                                          self.course))
        
        print("Students enrolled are: < {} >.".format(', '.join(self.enrolled_students)))
        
    def average_grade(self):
        grades = input('Gives a list of grades :')
        try:
            grades = eval(grades)
            if type(grades) == float or type(grades) == int:
                print("Average grade is {}".format(grades))
            else:
                print("Average grade is {}".format(sum(grades)/len(grades)))
                
        except Exception as e :
            print('Error is ', e)
        
    def complete(self, student_name):
        
        if student_name in self.enrolled_students:
            self.completed_students.append(student_name)
            self.enrolled_students.remove(student_name)
        else:
            print('{} not in course'.format(student_name))
            pass
            
        
        
OOP = Online("OOP", "Josh")

OOP.enroll("Nicolas Marois")
OOP.enroll("Nicolas Marois")
print()

OOP.enroll("Another student")
OOP.get_course_details()
OOP.complete("Nicolas Marois")
OOP.get_course_details()
