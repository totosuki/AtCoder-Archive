N,K = map(int,input().split())
A = list(map(int,input().split()))
print(*A[N-K:],*A[:N-K],sep=" ")