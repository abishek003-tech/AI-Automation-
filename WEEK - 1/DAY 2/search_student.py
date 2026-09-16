students = [
    {"name": "Arun", "mark": 78},
    {"name": "Priya", "mark": 92},
    {"name": "Santhiya", "mark": 92},
    {"name": "Karthik", "mark": 65}
]

def search_student(students, name):

    for student in students:
    
        if student["name"].lower() == name.lower():

            print("Name:", student["name"])
            print("Mark:", student["mark"])
            return
    
    print("Student not found")
    
while True:
    name = input("Enter student name to search (or 'exit' to quit): ")
    
    if name.lower() == 'exit':
        break
    
    search_student(students, name)


