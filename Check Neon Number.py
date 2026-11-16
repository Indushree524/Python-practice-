num = int(input("Enter a number: "))

square = num * num
total = 0

while square > 0:
    digit = square % 10
    total += digit
    square //= 10

if total == num:
    print("Neon Number")
else:
    print("Not a Neon Number")
