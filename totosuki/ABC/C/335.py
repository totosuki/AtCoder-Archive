import sys
input = sys.stdin.buffer.readline

N, Q = map(int, input().split())
pos = (1, 0)
vec = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
que = []
for i in range(N, 0, -1):
  que.append((i, 0))

for _ in range(Q):
  a, b = input().decode().rstrip().split()
  if a == "1":
    px, py = pos
    vx, vy = vec[b]
    px += vx
    py += vy
    pos = (px, py)
    que.append(pos)
  else:
    b = int(b)
    x, y = que[-b]
    print(x, y)