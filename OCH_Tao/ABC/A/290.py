N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0
for i in B:
  cnt+=A[i-1]
print(cnt)