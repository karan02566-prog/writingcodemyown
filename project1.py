# books = {
#     "title" : "harry potter",
#     "author" : "J. K. Rowling",
#     "pages" : 300
# }

# print(books["pages"])

# student = {
#     "name": "Karan",
#     "age": 19,
# }

# student["age"] = 20
# student["course"] = "geography"
# print(student["age"])
# print(student["name"])
# print(student["course"])
# print(student.get("city", "city not found"))

# game = {
#     "name": "Minecraft",
#     "price": 1000
# }

# game["price"] = 800
# game["rating"] = 9
# print(game["price"])
# print(game["rating"])

# for x in student:
#     print(x)


# print(student["age"])

# car = {
#     "brand": "Toyota",
#     "model": "Fortuner",
#     "year": 2025
# }

# for k, v in car.items():
#     print(k, ":", v)


# student = {
#     "name": "Karan",
#     "age": 19,
#     "course": "Geography"
# }

# for minion, monster in student.items():
#     print("the", minion, "is", monster)   

# student = {
#     "name": "Karan",
#     "marks": {
#         "english": 78,
#         "maths": 91
#     }
# }

# x=student["marks"]["maths"]
# print(x)

# students = {
#     "karan": {
#         "age": 19
#     },
#     "rahul": {
#         "age": 20
#     }
# }

# name = input("Enter your name: ")
# if name in students:
#     print(students[name]["age"])
# else:
#     print("student not found")
# x =students["Karan"]["age"]
# print(x)

# name = "Sanjana"

# y=students[name]["age"]
# print(y)

# name = input("enter your name: ")
# print(name)

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

#Enter student name: karan
#Enter subject: history
# name = input("enter student's name: ")
# subject = input("enter the subject: ")
# print(marks.get(name))
# print(marks[name][subject])\
name = input("enter student's name: ")
subject = input("enter the subject: ")
if name in marks:
    if subject in marks[name]:
        print(marks[name][subject])
    
    else:
        print("subject not found")
    
else:
    print("student not found)")
    

