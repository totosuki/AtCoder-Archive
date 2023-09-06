import sys
input = sys.stdin.buffer.readline

N = int(input())
P = list(map(int, input().split()))
cnt = 1
bf = P[0]

for i in range(1, N):
  now = P[i]
  if bf >= now:
    cnt += 1
    bf = now

print(cnt)