A,B,K = map(int,input().split())
X = min(A,K)
A-=X
K-=X
Y = min(B,K)
B-=Y
K-=Y
print(f"{A} {B}")