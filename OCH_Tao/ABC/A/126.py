N,K = map(int,input().split())
S = input()
x = S[0:K-1]
y = S[K-1]
z = S[K:]
print(x+y.lower()+z)