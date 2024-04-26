N = int(input())
W = list(map(int,input().split()))
cnt = []
for i in range(1,N):
  X = sum(W[:i])
  Y = sum(W[i:])
  cnt.append(abs(X-Y))
print(min(cnt))