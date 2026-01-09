#Minor Project: Student Data Analysis
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("student_marks_pandas.csv")

# Ask student name
name = input("Enter student name: ")

# Filter student data
student_data = df[df["Student Name"].str.lower() == name.lower()]

if student_data.empty:
    print("Student not found!")
else:
    # Select only marks columns
    marks = student_data[["PPL", "DSA", "M3", "OS", "DLED"]].iloc[0]

    # Mathematical calculations
    mean_marks = marks.mean()
    min_marks = marks.min()
    max_marks = marks.max()
    average_marks = marks.mean()
    total_marks = marks.sum()
    percentage = (total_marks / 500) * 100

    # Display results
    print("\n--- Student Performance Report ---")
    print(f"Student Name : {name}")
    print(f"Marks        :\n{marks}")
    print(f"\nMean         : {mean_marks:.2f}")
    print(f"Minimum      : {min_marks}")
    print(f"Maximum      : {max_marks}")
    print(f"Average      : {average_marks:.2f}")
    print(f"Percentage   : {percentage:.2f}%")

    # Graphical representation
    plt.figure()
    marks.plot(kind='bar')
    plt.title(f"Marks of {name}")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.grid(axis='y')
    plt.show()
