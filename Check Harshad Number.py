num = int(input("Enter a number: "))

temp = num
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

if temp > 0 and temp % total == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
