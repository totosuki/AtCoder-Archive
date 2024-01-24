N,X = map(int,input().split())
A = list(map(int,input().split()))
L = list(bin(X).zfill(N))
L.reverse()
cnt = 0
for i in range(N):
  if L[i] == "1":
    cnt += A[i]
print(cnt)