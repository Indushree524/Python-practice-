import math

ab = int(input())
bc = int(input())

angle = round(math.degrees(math.atan(ab / bc)))

print(str(angle) + "°")
