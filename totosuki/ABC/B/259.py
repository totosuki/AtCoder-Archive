import sys, math
input = sys.stdin.buffer.readline

a, b, d = map(int, input().split())

dist = math.sqrt(a**2 + b**2)
theta = math.atan2(b, a)

theta = theta + math.radians(d)

x = math.cos(theta) * dist
y = math.sin(theta) * dist

print(x, y)