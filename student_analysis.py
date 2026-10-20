import csv
import json

students = []

with open("student.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = [
            int(row["Maths"]),
            int(row["Science"]),
            int(row["English"]),
            int(row["Computer"])
        ]

        average = sum(marks) / len(marks)

        students.append({
            "Roll_No": row["Roll_No"],
            "Name": row["Name"],
            "Average": round(average, 2)
        })

with open("summary.json", "w") as file:
    json.dump(students, file, indent=4)

print("Student analysis completed!")
print("Summary saved to summary.json")