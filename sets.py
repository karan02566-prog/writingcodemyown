# s = set()
# print(type(s))

# x ={2, 5, 4, 7, 8, 1, 6, 8, 4, 3, 7, 8, 4, 7}
# print(x)

# set methods
#1 union

# x = {2, 4, 5, 7, 4, 8, 8, 2}
# y = {23, 75, 35, 67, 35, 94}
# z = x.union(y)
# print(z)

# update
x = {2, 4, 5, 7, 4, 8, 8, 2}
y = {23, 75, 35, 67, 35, 94}
x.update(y)
print(x)


# symmetric difference

a = {"delhi", "mumbai", "banglore", "jammu"}
b = {"bombay", "delhi", "jammu", "jabalpur", "banglore"}
c = a.symmetric_difference(b)
print(c)

# difference()

cities = {"delhi", "seoul", "tokyo", "new york"}
cities2 = {"delhi", "tokyo", "north atlanta", "california"}
print(cities.difference(cities2))

# isdisjoint

cities = {"delhi", "seoul", "tokyo", "new york"}
cities2 = {"delhi", "tokyo", "north atlanta", "california"}
print(cities.isdisjoint(cities2))


cities = {"delhi2", "seoul", "tokyos", "new york"}
cities2 = {"delhi", "tokyo", "north atlanta", "california"}
print(cities.isdisjoint(cities2))


# issuperset()

cities = {"delhi", "seoul", "tokyo", "new york"}
cities2 = {"delhi", "tokyo"}
print(cities.issuperset(cities2))


cities = {"delhi2", "seoul", "tokyos", "new york"}
cities2 = {"delhi", "tokyo", "north atlanta", "california"}
print(cities.issuperset(cities2))

# remove
cities = {"delhi", "seoul", "tokyo", "new york"}
cities.remove("tokyo")
print(cities)

# check if an item exists in a list

cities2 = {"delhi", "tokyo", "north atlanta", "california"}
if "north atlanta" in cities2:
    print ("yes it is there")
else:
    print("it's not here")