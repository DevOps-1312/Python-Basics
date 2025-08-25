student_info = [
    {
        "name": "John Doe",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.5,
        "enrolled": True,
        "courses": ["Data Structures", "Algorithms", "Operating Systems"]
    },
    {
        "name": "Jane Smith",
        "age": 22,
        "major": "Mathematics",
        "gpa": 3.8,
        "enrolled": True,
        "courses": ["Calculus", "Linear Algebra", "Statistics"]
    },
    {
        "name": "Alice Johnson",
        "age": 21,
        "major": "Physics",
        "gpa": 3.6,
        "enrolled": False,
        "courses": ["Quantum Mechanics", "Thermodynamics"]
    }
]


print("Total number of students:", len(student_info))
print("1st student's name:", student_info[0]["name"])
print("last student's major:", student_info[2]["major"])
print("list of all the students' names:")
for i in range (len(student_info)):
    print(student_info[i]["name"])
print("List of all the students' courses:")
for student in student_info:
    print(f"{student['name']}: {', '.join(student['courses'])}")
