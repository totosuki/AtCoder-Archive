N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
cntA = 0
cntB = 0
for i in range(N):
  cntA+=A[i]
  cntB+=B[i]
  if cntA>X or cntB>Y:
    print(i+1)
    break
else:
  print(N)