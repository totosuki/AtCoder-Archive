from math import sqrt
N = int(input())
O = []
for i in range(N):
  O.append(list(map(int,input().split())))
cnt = 0
for i in O:
  for j in O:
    cnt = max((i[0]-j[0])**2+(i[1]-j[1])**2,cnt)
print(sqrt(cnt))