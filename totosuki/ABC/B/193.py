import sys
input = sys.stdin.buffer.readline

N = int(input())
rslt = set()

for _ in range(N):
  A, P, X = map(int, input().split())
  if X > A:
    rslt.add(P)

if rslt:
  print(min(rslt))
else:
  print(-1)