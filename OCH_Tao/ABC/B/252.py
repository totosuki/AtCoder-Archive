N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
X = set([i+1 for i,j in enumerate(A) if j==max(A)])
for i in B:
  if i in X:
    print("Yes")
    break
else:
  print("No")