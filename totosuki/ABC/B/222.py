import sys
input = sys.stdin.buffer.readline

N, P = map(int, input().split())
A = tuple(map(int, input().split()))
cnt = 0

for a in A:
  if a < P:
    cnt += 1

print(cnt)