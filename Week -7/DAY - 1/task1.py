# T1 - Basic Probability

total_students = 60
python_students = 35
sql_students = 25
both_students = 15

# 1. Probability of Python
p_python = python_students / total_students

# 2. Probability of SQL
p_sql = sql_students / total_students

# 3. Probability of both
p_both = both_students / total_students

# 4. Python but not SQL
python_only = python_students - both_students
p_python_only = python_only / total_students

print("Probability of Python:", p_python)
print("Probability of SQL:", p_sql)
print("Probability of Both:", p_both)
print("Probability of Python but not SQL:", p_python_only)
