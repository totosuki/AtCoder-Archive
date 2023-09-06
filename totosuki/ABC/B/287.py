N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
count = 0
for s in S:
  for t in T:
    if s[3:] == t:
      count += 1
      break
print(count)