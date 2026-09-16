
#  \*T2  Student Database - Sample template

# students = [
#     {"name": "Arun", "mark": 78},
#     {"name": "Priya", "mark": 92},
#     {"name": "Karthik", "mark": 65},
#     {"name": "Divya", "mark": 88}
# ]

# Do the following tasks:

# Find topper
# Find average
# Find students above 80
# Find lowest scorer
# Count students above average*\


# ----------------------------------------------------------------------------------------


students= [  {"name": "Arun", "mark": 78},
    {"name": "Priya", "mark": 92},
    {"name": "Karthik", "mark": 65},
    {"name": "Divya", "mark": 88}
             
    ]
topper= students[0]
for student in students:
    if student["mark"] > topper ["mark"]:
        topper =student
print ("topper:",topper["name"],topper["mark"])

total =0
for student in students:
    total = total + student["mark"]
    avg = total / len(students)
print("Average :",avg)

lowest = students[0]

for student in students:
    if student["mark"] < lowest["mark"]:
        lowest = student

print("Lowest scorer:", lowest["name"], lowest["mark"])

count = 0

for student in students:
    if student["mark"] > average:
        count += 1

print("Students above average:", count)
