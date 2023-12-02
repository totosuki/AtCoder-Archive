H,W,N = map(int,input().split())
u = 2
li = [[0]*(W+u) for i in range((H+u))]

for i in range(N):
  A,B,C,D = map(int,input().split())
  li[A][B] += 1
  li[C+1][D+1] += 1
  li[C+1][B] -= 1
  li[A][D+1] -= 1

for i in range(1,H+2):
  for l in range(1,W+2):
    li[i][l] += li[i][l-1]

for i in range(1,H+2):
  for l in range(1,W+2):
    li[i][l] += li[i-1][l]

for i in range(1,H+1):
  print(*li[i][1:-1])