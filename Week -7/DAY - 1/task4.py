# T4 - Placement Probability

p_placed = 0.60
p_internship_given_placed = 0.80
p_internship_given_not_placed = 0.30

# Assume 100 students
total_students = 100

# Number of placed students
placed_students = total_students * p_placed

# Number of not placed students
not_placed_students = total_students - placed_students

# Internship students among placed
internship_and_placed = (
    placed_students * p_internship_given_placed
)

# Internship students among not placed
internship_and_not_placed = (
    not_placed_students * p_internship_given_not_placed
)

# Total internship students
total_internship = (
    internship_and_placed + internship_and_not_placed
)

# Probability of placed given internship
p_placed_given_internship = (
    internship_and_placed / total_internship
)

print("Placed students:", placed_students)
print("Not placed students:", not_placed_students)
print("Internship and placed:", internship_and_placed)
print("Internship and not placed:", internship_and_not_placed)
print("Total internship students:", total_internship)

print(
    "P(Placed | Internship):",
    p_placed_given_internship
)

print(
    "Percentage:",
    p_placed_given_internship * 100,
    "%"
)
