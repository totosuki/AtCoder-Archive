N,K,X = map(int,input().split())
A = list(map(int,input().split()))
print(*A[:K],X,*A[K:],sep=" ")