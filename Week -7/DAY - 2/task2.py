import pandas as pd

# Create DataFrame
data = {
    "Student_ID": ["S101", "S102", "S103", "S104",
                   "S105", "S106", "S107", "S108"],

    "Department": ["AI&DS", "CSE", "AI&DS", "CSE",
                   "IT", "AI&DS", "IT", "CSE"],

    "Attendance": [85, 72, 90, 80, 68, 88, 78, 92],

    "Python": [88, 91, 76, 95, 72, 89, 84, 87],

    "SQL": [78, 85, 82, 90, 75, 92, 80, 94],

    "Aptitude": [82, 88, 79, 92, 70, 85, 86, 90]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# # 1. Attendance > 75
# print("\nStudents with Attendance > 75:")
# print(df[df["Attendance"] > 75])

# # 2. Python > 80
# print("\nStudents with Python > 80:")
# print(df[df["Python"] > 80])

# # # 3. Department-wise average marks
# print("\nDepartment-wise Average:")
# print(df.groupby("Department")[[
#     "Python", "SQL", "Aptitude"
# ]].mean())

# 4. Calculate total marks
df["Total"] = df["Python"] + df["SQL"] + df["Aptitude"]

print("\nTotal Marks:")
print(df[["Student_ID", "Total"]])

# 5. Sort by total marks
sorted_students = df.sort_values("Total", ascending=0)

print("\nStudents sorted by Total:")
print(sorted_students)

# # 6. Top 5 students
# print("\nTop 5 Students:")
# print(sorted_students.head(5))