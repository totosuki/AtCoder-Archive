import itertools

N, M = map(int, input().split())
S = [input() for _ in range(N)]
combos = list(itertools.combinations(range(N), r = 2))
rslt = len(combos)

for combo in combos:
  for i in range(M):
    if S[combo[0]][i] == "x" and S[combo[1]][i] == "x":
      rslt -= 1
      break
print(rslt)