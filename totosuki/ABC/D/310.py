import sys, itertools
input = sys.stdin.buffer.readline

N, T, M = map(int, input().split())
team_l = [[] for _ in range(T)]
menber = list(range(1, N+1))
se = set()
cnt = 0

for _ in range(M):
  A, B = map(int, input().split())
  se.add((A, B))

# make team
for i in range(T):
  for n in range(1, N-T+2):
    for comb in itertools.combinations(menber, n):
      team_l[i].append(comb)

team_l_2 = [list(team) for team in itertools.product(*team_l) if len(list(itertools.chain.from_iterable(team))) == N]
team_l_3 = list()

for team in team_l_2:
  if len(set(itertools.chain.from_iterable(team))) == N:
    team_l_3.append(team)

print(team_l_3)

for team in team_l_3:
  flag = True
  for i in range(T):
    for j in range(len(team[i])):
      for k in range(j+1, len(team[i])):
        if (team[i][j], team[i][k]) in se:
          flag = False
  
  if flag:
    cnt += 1

print(cnt)