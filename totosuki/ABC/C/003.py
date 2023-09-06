import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
R = list(map(int, input().split()))
C = 0

R.sort(reverse = True)

for r in reversed(R[:K]):
  C = (C + r) / 2

print(C)