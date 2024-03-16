import math
import numpy as np
import os
import zipfile

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = []
        self.credits = []

    def calculate_gpa(self):
        if not self.marks or not self.credits:
            return 0
        weighted_marks = np.array(self.marks) * np.array(self.credits)
        return np.sum(weighted_marks) / np.sum(self.credits)

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

class Mark:
    def __init__(self, student, course, mark):
        self.student = student
        self.course = course
        self.mark = mark

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        num_students = int(input("Enter number of students to input: "))
        for _ in range(num_students):
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB: ")
            self.students.append(Student(id, name, dob))
        with open('students.txt', 'w') as f:
            for student in self.students:
                f.write(f'{student.id},{student.name},{student.dob}\n')

    def input_courses(self):
        num_courses = int(input("Enter number of courses to input: "))
        for _ in range(num_courses):
            id = input("Enter course id: ")
            name = input("Enter course name: ")
            credit = int(input("Enter course credit: "))
            self.courses.append(Course(id, name, credit))
        with open('courses.txt', 'w') as f:
            for course in self.courses:
                f.write(f'{course.id},{course.name},{course.credit}\n')

    def input_marks(self):
        course_id = input("Select a course by id: ")
        course = next((course for course in self.courses if course.id == course_id), None)
        if course is None:
            print("Course not found.")
            return
        for student in self.students:
            mark = float(input(f"Enter mark for student {student.name} in course {course_id}: "))
            mark = math.floor(mark * 10) / 10  # round down to 1 decimal place
            self.marks.append(Mark(student, course, mark))
            student.marks.append(mark)
            student.credits.append(course.credit)
        with open('marks.txt', 'w') as f:
            for mark in self.marks:
                f.write(f'{mark.student.id},{mark.course.id},{mark.mark}\n')

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(course.id, course.name)

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(student.id, student.name, student.dob)

    def show_marks(self):
        course_id = input("Select a course by id to show marks: ")
        for mark in self.marks:
            if mark.course.id == course_id:
                print(f"Mark for student {mark.student.name} in course {course_id}: {mark.mark}")

    def show_gpa(self):
        student_id = input("Select a student by id to show GPA: ")
        student = next((student for student in self.students if student.id == student_id), None)
        if student is None:
            print("Student not found.")
            return
        print(f"GPA for student {student.name}: {student.calculate_gpa()}")
        
def compress_files():
    with zipfile.ZipFile('students.dat', 'w') as zipf:
        for file in ['students.txt', 'courses.txt', 'marks.txt']:
            if os.path.exists(file):
                zipf.write(file)

def decompress_files():
    if os.path.exists('students.dat'):
        with zipfile.ZipFile('students.dat', 'r') as zipf:
            zipf.extractall()

def main():
    decompress_files()
    usth = School()
    usth.input_students()
    usth.input_courses()
    usth.list_courses()
    usth.list_students()
    num = int(input("Enter number of courses that you have inputted: "))
    for _ in range(num):
        usth.input_marks()
        usth.show_marks()
        usth.show_gpa()
    compress_files()

if __name__ == "__main__":
    main()