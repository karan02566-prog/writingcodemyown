# x = 10
# y = 3

# print(x / y)
# print(x // y)
# print(x % y)

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

num = int(input("enter a number: "))

if num % 2 == 0:
    print("num is even")
else:
    print("num is odd")


def power(x, n=2):
    return(x*x) 


print(power(5))