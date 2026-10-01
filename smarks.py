name = input("Enter student name: ")

marks = {
    "Python": int(input("Enter Python marks: ")),
    "Maths": int(input("Enter Maths marks: ")),
    "Geography": int(input("Enter Geography marks: "))
}

total = sum(marks.values())
average = total / len(marks)

print("Student:", name)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)