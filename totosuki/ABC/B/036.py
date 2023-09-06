N = int(input())
S = [list(input()) for _ in range(N)]
ans = []

for col in range(N):
  tmp = []
  for row in reversed(range(N)):
    tmp.append(S[row][col])
  ans.append(tmp)

[print("".join(l)) for l in ans]