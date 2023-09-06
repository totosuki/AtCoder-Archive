import sys
input = sys.stdin.buffer.readline

H, W = map(int, input().split())
A = [a for _ in range(H) for a in tuple(map(int, input().split()))]
rslt = 0
min_n = min(A)

for a in A:
  rslt += a - min_n

print(rslt)