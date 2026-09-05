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

# countries = ("spain", "usa", "china", "india", "new zeleand")
# temp = list(countries)
# temp.pop(4)
# countries = tuple(temp)
# print(countries)

# countries2 = ("laoPDR", "finland", "germany", "france")
# world = countries + countries2
# print(world)

numbers = (2, 5, 6, 7, 8, 14, 5, 4, 5, 9, 5)

# res = numbers.count(5)

# print(res)

# palm = numbers.index(8)
# print(palm)

palm = numbers.index(9, 3, 10)
print(palm)