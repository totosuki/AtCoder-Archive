N = int(input())
A = list(map(int,input().split()))
for i in range(N-1):
  S,T = map(int,input().split())
  if A[i]>=S:
    A[i+1]+=(A[i]//S)*T
    A[i]%=S
print(A[-1])