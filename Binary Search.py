A = [3, 8, 15, 22, 29, 37, 44, 51, 60]
target = 37

low = 0
high = len(A) - 1

while low <= high:
    mid = (low + high) // 2
    print(A[mid])

    if A[mid] == target:
        break
    elif A[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
