n = int(input("Enter number of terms: "))

a = 0
b = 1
lst = []

for i in range(n):
    lst.append(a)
    a, b = b, a + b

print("Reverse Fibonacci:", lst[::-1])
