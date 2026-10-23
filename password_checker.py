password = input("Enter a sample password to check: ")

score = 0

if len(password) >= 8:
    score += 1

if any(c.isupper() for c in password):
    score += 1

if any(c.islower() for c in password):
    score += 1

if any(c.isdigit() for c in password):
    score += 1

if any(not c.isalnum() for c in password):
    score += 1

print("\nPassword Strength:")

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Moderate")
else:
    print("Strong")
