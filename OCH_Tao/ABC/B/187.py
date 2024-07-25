from itertools import combinations
N = int(input())
L = []
for i in range(N):
  L.append(list(map(int,input().split())))
P = combinations(L,2)
print(len([i for i in list(map(lambda x:(x[0][1]-x[1][1])/(x[0][0]-x[1][0]),P)) if -1<=i<=1]))