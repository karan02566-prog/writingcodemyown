# student = {
# "name": "Karan",
# "age": 19,
# "college": "Shivaji"
# }

# x = student["college"]
# print(x)


# students = {
# "karan": {"age": 19},
# "sanjana": {"age": 20}
# }
# Ask for the name
# Then print the student's age

# name = input("enter your name: ")
# x = students[name]["age"]
# print(x)


marks = {
"karan": {
"english": 78,
"history": 83,
"science": 80
},
"sanjana": {
"english": 87,
"history": 45,
"science": 84
}
}
# Ask for student name
# Ask for subject
# Check student
# Check subject
# Print mark / error message
name = input("enter student's name: ")
subject = input("enter subject: ")

if name in marks:
    if subject in marks[name]:
        print(marks[name][subject])
    else:
        print("check the details again")
else:
    print("student not found")
