x = float(input("Enter x: "))
n = int(input("Enter n: "))

i = 1
term = 1      # will hold x^i / i!
total = 0

while i <= n:
    term = term * x / i     # builds each term from the previous one
    total = total + term
    i += 1

print("Sum =", total)

x = float(input("Enter x: "))
n = int(input("Enter n: "))

i = 0
term = 1      # x^0 = 1
total = 0

while i <= n:
    total = total + term
    term = term * x      # term becomes x^(i+1) for next round
    i += 1

print("Sum =", total)