N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0
X = set()
Y = set()
for i in range(N):
  if A[i]==B[i]:
    cnt+=1
  else:
    X.add(A[i])
    Y.add(B[i])
print(cnt)
print(len(X&Y))