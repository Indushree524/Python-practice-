import heapq

h = []

heapq.heappush(h, 40)
heapq.heappush(h, 10)
heapq.heappush(h, 30)
heapq.heappush(h, 5)
heapq.heappush(h, 20)

print(heapq.heappop(h))
print(heapq.heappop(h))
print(len(h))
