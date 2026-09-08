for i in range(9):
    if i == 6:
        print("6 is there")
    else:
        print("6 is not there")


numbers = [2, 4, 6, 8, 10]

for num in numbers:
    if num == 5:
        print("Found 5")
        break
else:
    print("5 was not found")



for x in range(7):
    print("iteration no {} is in the loop".format(x+1))
else:
    print("loop is over now")
