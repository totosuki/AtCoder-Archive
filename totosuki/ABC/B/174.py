import math
N, D = map(int, input().split())
cnt = 0

for i in range(N):
  X, Y = map(int, input().split())
  dist = math.sqrt(X**2 + Y**2)
  if dist <= D:
    cnt += 1

print(cnt)