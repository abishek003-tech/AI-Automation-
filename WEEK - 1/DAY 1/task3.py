

# Create a function : validate_age(age)
# Rules:
# Age must be between 1 and 100
# If valid → "Valid"
# Otherwise → "Invalid"

# Then extend it :

# validate_student(name, age, mark)

def validate_student(name, age, mark):
    if name == "" or  age< 1 or age > 100 or  mark < 0 or mark > 100:
        return "Invalid"
    
    else:
        return "Valid"

name = input("Enter student name: ")
age = int(input("Enter age: "))
mark = int(input("Enter mark: "))

print(validate_student(name, age, mark))