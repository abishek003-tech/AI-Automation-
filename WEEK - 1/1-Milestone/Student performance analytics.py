#CASE STUDY 1 — Student Performance Analytics
#Given data
#students = [
# {"name": "Arun", "department": "BCA", "mark": 78},
# {"name": "Meena", "department": "BSc CS", "mark": 91},
#    {"name": "Rahul", "department": "BCA", "mark": 45},
#    {"name": "Divya", "department": "BSc AI", "mark": 67},
#    {"name": "Karthik", "department": "BCA", "mark": 32},
#    {"name": "Priya", "department": "BSc AI", "mark": 88}
#]
#1. Understand the Problem
#
#find:
#
#Highest mark
#Average mark
#Students below 50
#Students above 75
#Department-wise average
#
#---------------------------------------------------------------------------------------------------------------
students = [
    {"name": "Arun", "department": "BCA", "mark": 78},
    {"name": "Meena", "department": "BSc CS", "mark": 91},
    {"name": "Rahul", "department": "BCA", "mark": 45},
    {"name": "Divya", "department": "BSc AI", "mark": 67},
    {"name": "Karthik", "department": "BCA", "mark": 32},
    {"name": "Priya", "department": "BSc AI", "mark": 88}
]

topper=students[0]
for student in students:
    if topper["mark"]>student["mark"]:
        topper=student
print("topper :",topper["name"],topper["mark"])

total = [0]
for student in students:
    total += students["mark"]
avg=total /len(students)
print ("Average :",avg)
