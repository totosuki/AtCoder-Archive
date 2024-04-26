N = int(input())
D,X = map(int,input().split())
A = []
for i in range(N):
  A.append(int(input()))
for i in range(1,D+1):
  for j in A:
    if j==1:
      X+=1
    elif i%j==1:
      X+=1
print(X)