N = int(input())
L = []
for i in range(N):
  A,C = map(int,input().split())
  L.append([A,C,i+1])
X = sorted(L,key=lambda x:x[1])
Y = []
for i in range(N-1):
  cnt = X.pop()
  if cnt[0]>max(X,key=lambda x:int(x[0]))[0]:
    Y.append(cnt[2])
else:
  Y.append(X[0][2])
print(len(Y))
print(*sorted(Y))