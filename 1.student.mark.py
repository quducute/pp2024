students = []
courses = []
marks = {}

def input_students():
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        students.append((id, name, dob))

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for _ in range(num_courses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append((id, name))

def input_marks():
    course_id = input("Select a course by id: ")
    for student in students:
        mark = input(f"Enter mark for student {student[1]} in course {course_id}: ")
        marks[(student[0], course_id)] = mark

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
    while True:
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("7. Exit")
        option = int(input("Select an option: "))
        if option == 1:
            input_students()
        elif option == 2:
            input_courses()
        elif option == 3:
            input_marks()
        elif option == 4:
            list_courses()
        elif option == 5:
            list_students()
        elif option == 6:
            show_marks()
        elif option == 7:
            break

if __name__ == "__main__":
    main()