N,X = map(int,input().split())
A = list(map(int,input().split()))
print("Yes" if sum(A)-N//2<=X else "No")