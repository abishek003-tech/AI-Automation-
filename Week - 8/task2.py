T2 - PART B: INSPECT THE DATA
# ============================================================

print("\n" + "=" * 60)
print("T2 - DATA INSPECTION")
print("=" * 60)

# Number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Data types
print("\nData Types:")
print(df.dtypes)

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())


# ============================================================
# T2 - HANDLE MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("HANDLING MISSING VALUES")
print("=" * 60)

# Separate numerical and categorical columns
numeric_columns = df.select_dtypes(include=np.number).columns
categorical_columns = df.select_dtypes(include="object").columns

# Fill numerical missing values with median
for column in numeric_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].median())

# Fill categorical missing values with mode
for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

print("Missing values handled.")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ============================================================
# T2 - REMOVE DUPLICATES
# ============================================================

print("\n" + "=" * 60)
print("REMOVING DUPLICATES")
print("=" * 60)

before = len(df)

df = df.drop_duplicates()

after = len(df)

print("Rows before removing duplicates:", before)
print("Rows after removing duplicates:", after)
print("Duplicates removed:", before - after)


# ============================================================
# T2 - VALIDATE NUMERICAL VALUES
# ============================================================

print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)

# Display possible invalid values for common student columns

if "CGPA" in df.columns:
    print("\nInvalid CGPA values:")
    print(df[(df["CGPA"] < 0) | (df["CGPA"] > 10)])

if "Attendance" in df.columns:
    print("\nInvalid Attendance values:")
    print(df[(df["Attendance"] < 0) | (df["Attendance"] > 100)])

if "Aptitude_Score" in df.columns:
    print("\nInvalid Aptitude Scores:")
    print(df[
        (df["Aptitude_Score"] < 0) |
        (df["Aptitude_Score"] > 100)
    ])

if "Technical_Score" in df.columns:
    print("\nInvalid Technical Scores:")
    print(df[
        (df["Technical_Score"] < 0) |
        (df["Technical_Score"] > 100)
    ])

if "Communication_Score" in df.columns:
    print("\nInvalid Communication Scores:")
    print(df[
        (df["Communication_Score"] < 0) |
        (df["Communication_Score"] > 100)
    ])