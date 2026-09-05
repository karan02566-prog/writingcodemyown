scores= [34, 67, 86, 36, 90, 81]

subjects = ["history", "english", "maths", "geography"]

pending_tasks = []

print(scores)
print(subjects)
print(pending_tasks)

print(scores[0])
print(scores[3])
print(subjects[2])

if any(80 <= score <= 99 for score in scores):
    print("you're good at studies")
else:
    print("you need to work hard")

if 50 in scores:
    print("yes it is there")
else:
    print("it's not there")

print(scores[-3])

print(subjects[len(subjects)-1])
if "english" in subjects:
    print("yes you can choose english")
else:
    print("we don't have english as an option")

print(scores[1:5:2])

# scores.append(55)
# print(scores)

# scores.sort()
# print(scores)

scores.insert(5,45)
print(scores)

x = [56, 49, 23, 72]

scores.extend(x)
print(scores)