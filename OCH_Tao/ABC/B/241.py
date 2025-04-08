from collections import Counter
N,M = map(int,input().split())
A = Counter(list(map(int,input().split())))
B = list(map(int,input().split()))
for i in B:
  if A[i]==0:
    print("No")
    break
  else:
    A[i]-=1
else:
  print("Yes")