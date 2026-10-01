# ==============================
# STUDENT PERFORMANCE EDA
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Load Dataset
df = pd.read_csv("student_performance.csv")

print("===== FIRST 5 ROWS =====")
print(df.head())


# 2. Dataset Shape
print("\n===== DATASET SHAPE =====")
print(df.shape)


# 3. Data Types
print("\n===== DATA TYPES =====")
print(df.dtypes)


# 4. Missing Values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# 5. Descriptive Statistics
print("\n===== DESCRIPTIVE STATISTICS =====")
print(df.describe())


# 6. Categorical Columns
categorical_columns = df.select_dtypes(
    include="object"
).columns

print("\n===== CATEGORICAL COLUMNS =====")

for column in categorical_columns:
    print("\n", column)
    print(df[column].unique())


# 7. Numerical Columns
numerical_columns = df.select_dtypes(
    include=np.number
).columns

print("\n===== NUMERICAL COLUMNS =====")
print(list(numerical_columns))


# ==============================
# VISUALIZATION
# ==============================

# 8. Histogram
plt.figure(figsize=(8,5))

plt.hist(
    df["Python_Mark"],
    bins=10
)

plt.xlabel("Python Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Python Marks")

plt.show()


# 9. Department Bar Chart
department_marks = df.groupby(
    "Department"
)["Python_Mark"].mean()

department_marks.plot(
    kind="bar",
    figsize=(8,5)
)

plt.xlabel("Department")
plt.ylabel("Average Python Marks")
plt.title("Average Python Marks by Department")

plt.show()


# ==============================
# RELATIONSHIP ANALYSIS
# ==============================

# 10. Attendance vs Marks
plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Attendance",
    y="Python_Mark"
)

plt.title("Attendance vs Python Marks")

plt.show()


# 11. Study Hours vs Marks
plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Python_Mark"
)

plt.title("Study Hours vs Python Marks")

plt.show()


# 12. Assignment Completion vs Marks
plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="Assignment_Completion",
    y="Python_Mark"
)

plt.title("Assignment Completion vs Python Marks")

plt.show()


# ==============================
# CORRELATION
# ==============================

correlation_matrix = df[
    numerical_columns
].corr()

print("\n===== CORRELATION MATRIX =====")
print(correlation_matrix)


# Correlation Heatmap
plt.figure(figsize=(10,7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")

plt.show()


# ==============================
# OUTLIER DETECTION
# ==============================

column = "Python_Mark"

Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df[column] < lower_limit) |
    (df[column] > upper_limit)
]

print("\n===== OUTLIERS =====")
print(outliers)


# Boxplot
plt.figure(figsize=(8,5))

sns.boxplot(
    x=df[column]
)

plt.title("Python Marks - Outlier Detection")

plt.show()