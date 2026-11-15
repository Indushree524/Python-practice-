num = int(input("Enter a number: "))
temp = num
total = 0

while num > 0:
    digit = num % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    num = num // 10

if total == temp:
    print("Strong Number")
else:
    print("Not a Strong Number")
