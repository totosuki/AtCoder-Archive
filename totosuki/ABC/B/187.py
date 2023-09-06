from itertools import combinations

data = [tuple(map(int, input().split())) for _ in range(int(input()))]
cnt = 0

for d in combinations(data, 2):
  rslt = (d[0][1]-d[1][1]) / (d[0][0]-d[1][0])
  if -1 <= rslt <= 1:
    cnt += 1

print(cnt)