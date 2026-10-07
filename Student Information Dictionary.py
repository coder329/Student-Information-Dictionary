# Student Information Dictionary
# Task 7 - Level 1 - Day 7

# Student records stored using a dictionary
students = {
    "S001": {
        "name": "Rahul",
        "age": 20,
        "course": "AI & ML",
        "marks": 85
    },
    "S002": {
        "name": "Priya",
        "age": 21,
        "course": "Data Science",
        "marks": 91
    },
    "S003": {
        "name": "Aman",
        "age": 19,
        "course": "Computer Science",
        "marks": 78
    }
}


# Search for a student
def search_student(student_id):
    if student_id in students:
        print("\nStudent Found:")
        print("Student ID:", student_id)

        for key, value in students[student_id].items():
            print(f"{key.title()}: {value}")
    else:
        print("\nStudent not found.")


# Add a new student
def add_student(student_id, name, age, course, marks):
    if student_id in students:
        print("\nStudent ID already exists.")
    else:
        students[student_id] = {
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }
        print("\nStudent added successfully.")


# Update student information
def update_student(student_id, field, value):
    if student_id in students:
        students[student_id][field] = value
        print("\nStudent information updated successfully.")
    else:
        print("\nStudent not found.")


# Display all students
def display_students():
    print("\n===== ALL STUDENT RECORDS =====")

    for student_id, information in students.items():
        print("\nStudent ID:", student_id)

        for key, value in information.items():
            print(f"{key.title()}: {value}")


# Display original records
display_students()

# Search operation
search_student("S002")

# Add operation
add_student(
    "S004",
    "Neha",
    20,
    "Artificial Intelligence",
    88
)

# Update operation
update_student(
    "S001",
    "marks",
    90
)

# Display updated records
display_students()