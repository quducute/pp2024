class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

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

    def input_courses(self):
        num_courses = int(input("Enter number of courses to input: "))
        for _ in range(num_courses):
            id = input("Enter course id: ")
            name = input("Enter course name: ")
            self.courses.append(Course(id, name))

    def input_marks(self):
        course_id = input("Select a course by id: ")
        for student in self.students:
            mark = input(f"Enter mark for student {student.name} in course {course_id}: ")
            self.marks.append(Mark(student, course_id, mark))

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
            if mark.course == course_id:
                print(f"Mark for student {mark.student.name} in course {course_id}: {mark.mark}")

def main():
    usth = School()
    usth.input_students()
    usth.input_courses()
    usth.list_courses()
    usth.list_students()
    num = int(input("Enter number of courses that you have inputted: "))
    for _ in range(num):
        usth.input_marks()
        usth.show_marks()

if __name__ == "__main__":
    main()