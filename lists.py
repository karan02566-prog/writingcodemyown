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
