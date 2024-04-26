N,M,X = map(int,input().split())
A = list(map(int,input().split()))
case0 = 0
caseN = 0
for i in range(X,-1,-1):
  if i in A:
    case0+=1
for i in range(X,N+1):
  if i in A:
    caseN+=1
print(min(case0,caseN))