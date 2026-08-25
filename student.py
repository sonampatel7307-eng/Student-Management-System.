class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print("\nStudent ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)


students = []


def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = Student(student_id, name, age, course, marks)
    students.append(student)

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
    else:
        print("\n===== STUDENT RECORDS =====")
        for student in students:
            student.display()


def search_student():
    student_id = int(input("Enter Student ID to search: "))

    for student in students:
        if student.student_id == student_id:
            print("\nStudent found!")
            student.display()
            return

    print("Student not found!")


def update_student():
    student_id = int(input("Enter Student ID to update: "))

    for student in students:
        if student.student_id == student_id:
            print("\nEnter new student details:")

            student.name = input("Enter New Name: ")
            student.age = int(input("Enter New Age: "))
            student.course = input("Enter New Course: ")
            student.marks = float(input("Enter New Marks: "))

            print("Student updated successfully!")
            return

    print("Student not found!")


def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")