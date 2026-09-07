# x = {
#     "name" : "karan",
#     "age" : 19,
#     "hobby" : "rading books",
#     "dream" : "masters abroad"

# }
# # print(x["dream"])
# print(x["hobby"])
# print(x["age"])
# print(x["name"])

# for key in x.keys():
#     print(x[key])

# methods

x = {
    "name" : "karan",
    "age" : 19,
    "hobby" : "rading books",
    "dream" : "masters abroad"

}

y = {
    "height" : "5'7",
    "college" : "shivaji college",

}

# x.update(y)
# print(x)

# x.pop("age")
# print(x)

y.popitem()
print(y)

# fromkey()

x.fromkeys("name")
print(x)
