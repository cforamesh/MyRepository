student_marks = {
    "Alice": 85,
    "Rambo": 92,
    "Harry": 78,
    "Tom": 88,
    "David": 95
}
Student_Name = input("Enter the Student's Name : ")
if Student_Name in student_marks:
    print(f"{Student_Name}'s marks: {student_marks[Student_Name]}")
else:
    print("Student not found.")