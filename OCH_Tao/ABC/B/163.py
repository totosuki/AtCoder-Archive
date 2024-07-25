N,M = map(int,input().split())
A = list(map(int,input().split()))
print(max(N-sum(A),-1))