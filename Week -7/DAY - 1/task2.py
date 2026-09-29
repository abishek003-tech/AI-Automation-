# T2 - Conditional Probability

total_students = 100
internship_students = 70
placed_students = 50
internship_and_placed = 40

# 1. Probability of being placed
p_placed = placed_students / total_students

# 2. Probability of placed given internship
p_placed_given_internship = internship_and_placed / internship_students

# 3. Probability of internship given placed
p_internship_given_placed = internship_and_placed / placed_students

print("P(Placed):", p_placed)
print("P(Placed | Internship):", p_placed_given_internship)
print("P(Internship | Placed):", p_internship_given_placed)
