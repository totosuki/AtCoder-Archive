import sys
input = sys.stdin.buffer.readline

N = int(input())
S = list()
T = list()
for _ in range(N):
  s, t = input().decode().strip().split()
  S.append(s)
  T.append(t)
answer = "Yes"

for i in range(N):
  if not S[i] in S[:i]+S[i+1:]+T[:i]+T[i+1:]:
    continue
  elif not T[i] in S[:i]+S[i+1:]+T[:i]+T[i+1:]:
    continue
  else:
    answer = "No"

print(answer)