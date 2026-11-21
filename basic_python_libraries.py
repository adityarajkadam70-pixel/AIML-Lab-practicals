import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

print("MATH LIBRARY")

print("Square Root:", math.sqrt(25))
print("Factorial:", math.factorial(5))
print("Ceiling:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Absolute Value:", math.fabs(-15))


print("\nNUMPY LIBRARY")

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))


print("\nPANDAS LIBRARY")

data = {
    "Student": ["A", "B", "C", "D", "E", "F"],
    "Math": [85, 90, np.nan, 70, 95, 80],
    "Science": [78, 88, 82, 75, 92, 85],
    "English": [80, 85, 79, 72, 90, 81]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

print("\nFirst Five Records:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

df["Math"] = df["Math"].fillna(df["Math"].mean())

print("\nCleaned Dataset:")
print(df)

print("\nSummary Statistics:")
print(df.describe())


print("\nSCIPY LIBRARY")

math_scores = df["Math"].to_numpy()
science_scores = df["Science"].to_numpy()

print("Mode:", stats.mode(math_scores, keepdims=False).mode)

correlation, p_value = stats.pearsonr(math_scores, science_scores)

print("Correlation:", correlation)


print("\nMATPLOTLIB VISUALIZATION")

plt.figure(figsize=(8, 5))
plt.plot(df["Student"], df["Math"], marker="o")
plt.title("Math Marks of Students")
plt.xlabel("Students")
plt.ylabel("Math Marks")
plt.grid(True)
plt.show()

average_marks = df[["Math", "Science", "English"]].mean()

plt.figure(figsize=(8, 5))
plt.bar(average_marks.index, average_marks.values)
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["Math"], df["Science"])
plt.title("Math vs Science Marks")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")
plt.show()
