N,X = map(int,input().split())
S = list(input())
for i in S:
  if i=="o":
    X+=1
  else:
    X=max(0,X-1)
print(X)