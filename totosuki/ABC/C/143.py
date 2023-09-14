import sys
input = sys.stdin.buffer.readline

N = int(input())
S = list(input().decode().rstrip())
cnt = 1
now = S[0]

for i in range(1, N):
  if S[i] != now:
    now = S[i]
    cnt += 1

print(cnt)