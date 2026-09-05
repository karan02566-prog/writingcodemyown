# tup = (2, 5, 6, 7, 8, 14)
# print(type(tup), tup)

# tup2 = tup[1:-2]
# print(tup2)

#maipulating tuples

# countries = ("spain", "usa", "china", "india","new zeleand")

# temp = list(countries)
# temp.append("australia")
# countries = tuple(temp)
# print(countries)

countries = ("spain", "usa", "china", "india", "new zeleand")
temp = list(countries)
temp.pop(4)
countries = tuple(temp)
print(countries)