import sys; from math import gcd
input = sys.stdin.buffer.readline

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
se = set()

for i in range(N):
  for j in range(N):
    if i == j: continue
    
    xi, yi = XY[i]
    xj, yj = XY[j]
    dx = xj - xi
    dy = yj - yi
    a = gcd(dx, dy)
    se.add((dx // a, dy // a))

print(len(se))