
# Task 1: Student data

students = [
    {
        "name": "Girish Khanna",
        "roll_no": "101",
        "aptitude": 95,
        "verbal": 95,
        "coding": 90
    },
    {
        "name": "Jankeesh Khanna",
        "roll_no": "102",
        "aptitude": 70,
        "verbal": 80,
        "coding": 75
    },
    {
        "name": "Aman Sharma",
        "roll_no": "103",
        "aptitude": 45,
        "verbal": 50,
        "coding": 35
    },
    {
        "name": "Aaryan Sharma",
        "roll_no": "104",
        "aptitude": 90,
        "verbal": 85,
        "coding": 95
    },
    {
        "name": "Shivansh Sharma",
        "roll_no": "105",
        "aptitude": 55,
        "verbal": 60,
        "coding": 50
    }
]

# Add another student through input()

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

new_student = {
    "name": name,
    "roll_no": roll_no
}

for subject in ["aptitude", "verbal", "coding"]:
    while True:
        score = int(input(f"Enter {subject} score (0-100): "))

        if 0 <= score <= 100:
            new_student[subject] = score
            break
        else:
            print("Invalid score! Enter between 0 and 100.")

students.append(new_student)

print("\nStudent records:")
for student in students:
    print(student)


# Task 2: Functions

# Calculate average marks
def average(student):
    total = (
        student["aptitude"]
        + student["verbal"]
        + student["coding"]
    )
    return total / 3


# Assign grade based on average
def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"


# Find student with highest average
def top_scorer(students):
    return max(students, key=average)


# Find students who need practice
def needs_practice(students, limit=40):
    result = []

    for student in students:
        if average(student) < limit:
            result.append(student)

    return result


# Display result table
print("\n========== STUDENT RESULT TABLE ==========")

print(f"{'Name':<12} {'Roll No':<10} {'Average':<10} {'Grade'}")
print("-" * 50)

for student in students:
    avg = average(student)
    student_grade = grade(avg)

    print(
        f"{student['name']:<12} "
        f"{student['roll_no']:<10} "
        f"{avg:<10.2f} "
        f"{student_grade}"
    )


# Display top scorer
top = top_scorer(students)

print("\nTop Scorer:", top["name"])
print("Highest Average:", round(average(top), 2))


# Display students needing practice
print("\nStudents Who Need Practice:")

practice_students = needs_practice(students)

for student in practice_students:
    print(student["name"], "-", round(average(student), 2))

