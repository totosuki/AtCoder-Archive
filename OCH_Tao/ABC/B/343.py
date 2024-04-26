N = int(input())
A = []
for i in range(N):
  A.append(list(map(int,input().split())))
for i in range(N):
  cnt = []
  for j in range(N):
    if A[i][j]==1:
      cnt.append(j+1)
  else:
    print(" ".join([str(i) for i in cnt]))