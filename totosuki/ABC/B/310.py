N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
answer = "No"

for i in range(N):
  for j in range(N):
    Pi, Pj = data[i][0], data[j][0]
    Fi, Fj = data[i][2:], data[j][2:]
    se = set(Fi) & set(Fj)
    
    if all([Pi >= Pj, len(se) == len(Fi), Pi > Pj or len(Fi) < len(Fj)]):
      answer = "Yes"

print(answer)