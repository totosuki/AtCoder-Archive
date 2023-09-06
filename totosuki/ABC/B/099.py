a, b = map(int, input().split())
diff = b - a
height = 0

for i in range(1,diff + 1):
  height += i

print(height - b)