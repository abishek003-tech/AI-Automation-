import pandas as pd
import numpy as np

# Create deliberately messy data

data = {
    "Student_ID": ["S101", "S102", "S103", "S103", "S104", "S105", "S106"],

    "Department": ["AI&DS", "CSE", "AI&DS", "AI&DS",
                   "CSE", "IT", "IT"],

    "Attendance": [85, 90, 75, 75, 105, "80", 70],

    "Python": [88, np.nan, 105, 105, 92, "85", 78],

    "SQL": [80, 85, 79, 79, np.nan, 88, 75],

    "Aptitude": [82, 90, 77, 77, 95, 86, 72]
}

df = pd.DataFrame(data)

# Number of records before cleaning
before = len(df)

print("Original Dataset:")
print(df)

print("\nNumber of records before cleaning:", before)

# # --------------------------------
# # 1. Check missing values
# # --------------------------------

# print("\nMissing Values:")
# print(df.isnull().sum())

# # --------------------------------
# # 2. Check duplicate rows
# # --------------------------------

# print("\nDuplicate Rows:")
# print(df[df.duplicated()])

# # --------------------------------
# # 3. Convert columns to numeric
# --------------------------------

df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")
df["Python"] = pd.to_numeric(df["Python"], errors="coerce")
df["SQL"] = pd.to_numeric(df["SQL"], errors="coerce")
df["Aptitude"] = pd.to_numeric(df["Aptitude"], errors="coerce")

# --------------------------------
# 4. Replace invalid values with NaN
# --------------------------------

df.loc[(df["Attendance"] < 0) | (df["Attendance"] > 100), "Attendance"] = np.nan

df.loc[(df["Python"] < 0) | (df["Python"] > 100), "Python"] = np.nan

df.loc[(df["SQL"] < 0) | (df["SQL"] > 100), "SQL"] = np.nan

df.loc[(df["Aptitude"] < 0) | (df["Aptitude"] > 100), "Aptitude"] = np.nan

# --------------------------------
# 5. Remove duplicates
# --------------------------------

df = df.drop_duplicates()

# --------------------------------
# 6. Handle missing values
# --------------------------------

df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

df["Python"] = df["Python"].fillna(df["Python"].mean())

df["SQL"] = df["SQL"].fillna(df["SQL"].mean())

df["Aptitude"] = df["Aptitude"].fillna(df["Aptitude"].mean())

# --------------------------------
# 7. Final validation
# --------------------------------

print("\nCleaned Dataset:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nNumber of records after cleaning:", len(df))