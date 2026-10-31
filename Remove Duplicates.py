numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original List:", numbers)
print("List after removing duplicates:", unique_numbers)
