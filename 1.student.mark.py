students = [] #list
courses = [] #list
marks = {} #dict

def input_students():
    num_students = int(input("Enter number of students to input: "))
    for _ in range(num_students):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        stuin4 = (id, name, dob) #tuple
        students.append(stuin4)

def input_courses():
    num_courses = int(input("Enter number of courses to input: "))
    for _ in range(num_courses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        couin4 = (id, name) #tuple
        courses.append(couin4)

def input_marks():
    course_id = input("Select a course by id: ")
    for student in students:
        mark = input(f"Enter mark for student {student[1]} in course {course_id}: ") #student[1] is student name
        marks[(student[0], course_id)] = mark #student[0] is student id

def list_courses():
    print("Courses:")
    for course in courses:
        print(course)

def list_students():
    print("Students:")
    for student in students:
        print(student)

def show_marks():
    course_id = input("Select a course by id to show marks: ")
    for student in students:
        print(f"Mark for student {student[1]} in course {course_id}: {marks[(student[0], course_id)]}")

def main():
    input_students()
    input_courses()
    list_courses()
    list_students()
    num = int(input("Enter number of courses that you have inputted: "))
    for _ in range(num):
        input_marks()
        show_marks()

if __name__ == "__main__":
    main()