import pandas as pd

df = pd.read_csv("student_marks_dirty_100.csv")

df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]
df = df.drop_duplicates()
highest = df["Marks"].max()


second_highest = df["Marks"].drop_duplicates().nlargest(2).iloc[-1]

average = df["Marks"].mean()

count_above_75 = (df["Marks"] > 75).sum()

print("Highest Mark:", highest)
print("Second Highest Mark:", second_highest)
print("Average Mark:", average)
print("Students Above 75:", count_above_75)