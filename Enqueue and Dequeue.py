from collections import deque

q = deque([1, 2, 3, 4, 5])

for i in range(3):
    x = q.popleft()
    q.append(x * 2)

print(*q)
