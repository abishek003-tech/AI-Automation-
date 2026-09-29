import pandas as pd


df = pd.read_csv("student_records.csv")

print("CSV Loaded Successfully")

# -------------------------
# 2. Understand dataset
# -------------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nNumber of Rows and Columns:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

# -------------------------
# 3. Check missing values
# -------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------
# 4. Check duplicates
# -------------------------

print("\nDuplicate Records:")
print(df.duplicated().sum())

# -------------------------
# 5. Statistical summary
# -------------------------

print("\nStatistical Summary:")
print(df.describe())

# -------------------------
# 6. Remove duplicates
# -------------------------

df = df.drop_duplicates()

# -------------------------
# 7. Handle missing values
# -------------------------

# Fill numerical columns with their mean
numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# -------------------------
# 8. Check again
# -------------------------

print("\nAfter Cleaning:")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nFinal Dataset:")
print(df)

# -------------------------
# 9. Summary Report
# -------------------------

print("\n========== SUMMARY REPORT ==========")

print("Total Records:", len(df))
print("Total Columns:", len(df.columns))

print("\nColumns:")
for column in df.columns:
    print("-", column)