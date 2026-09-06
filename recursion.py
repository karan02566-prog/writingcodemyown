# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# n = int(input("choose a number: "))
# print(factorial(n))

# fibonacci sequence
def fibonacci(num):
    if(num==0 or num==1):
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

n = int(input("give me a number: "))

print(fibonacci(n-1) + (n-2))

# for i in range(n + 1):
#     print(fibonacci(i), end=" ")

    