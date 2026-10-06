import pandas as pd

data = {
    "CGPA": [7.2, 8.1, 6.8, 9.0, 7.5, 8.4, 5.9, 9.2, 7.8, 8.0]
}

df = pd.DataFrame(data)

# Mean
print("Mean:", df["CGPA"].mean())

# Median
print("Median:", df["CGPA"].median())

# Standard deviation
print("Standard Deviation:", df["CGPA"].std())

# Percentiles
print("25th Percentile:", df["CGPA"].quantile(0.25))
print("50th Percentile:", df["CGPA"].quantile(0.50))
print("75th Percentile:", df["CGPA"].quantile(0.75))

# Outliers
Q1 = df["CGPA"].quantile(0.25)
Q3 = df["CGPA"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["CGPA"] < lower) |
    (df["CGPA"] > upper)
]

print("\nPossible Outliers:")
print(outliers)