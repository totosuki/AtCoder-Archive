from itertools import permutations

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = 10

S = sorted(S, key = lambda x: x.count("o"), reverse = True)

for perm in permutations(range(N)):
  seen = [False] * M
  cnt = 0
  for i in range(N):
    cnt += 1
    if cnt >= ans:
      break
    for j in range(M):
      if not seen[j] and S[perm[i]][j] == "o":
        seen[j] = True
    if all(seen):
      ans = min(ans, cnt)
      break

print(ans)