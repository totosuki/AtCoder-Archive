from itertools import combinations
from math import sqrt
N = int(input())
L = []
for i in range(N):
  L.append(list(map(int,input().split())))
C = combinations(L,2)
ans = 0
for i in C:
  ans=max(ans,sqrt((i[0][0]-i[1][0])**2+(i[0][1]-i[1][1])**2))
print(ans)