import pandas as pd

# Ask number of students
n = int(input("Enter number of students: "))

students = []

# Take input in dictionary form
for i in range(n):
    print(f"\nEnter details for student {i+1}")

    student = {
        "Student Name": input("Student Name: "),
        "PPL": int(input("PPL Marks: ")),
        "DSA": int(input("DSA Marks: ")),
        "M3": int(input("M3 Marks: ")),
        "OS": int(input("OS Marks: ")),
        "DLED": int(input("DLED Marks: "))
    }

    students.append(student)

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(students)

# Create new CSV file
df.to_csv("student_marks_pandas.csv", index=False)

print("\nCSV file 'student_marks_pandas.csv' created successfully using pandas!")
