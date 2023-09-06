import sys; from collections import deque
input = sys.stdin.buffer.readline

N, A, B = map(int, input().split())
S = deque(input().decode().strip())
rslt = float("inf")

for i in range(N):
  if i != 0:
    S_0 = S.popleft()
    S.append(S_0)
  cnt = 0
  for j in range(N//2):
    if S[j] != S[-j-1]:
      cnt += 1

  tmp = (i * A) + (cnt * B)
  rslt = min(rslt, tmp)

print(rslt)