A,B,C,K = map(int,input().split())
S,T = map(int,input().split())
x = A * S + B * T
if K <= S + T:
  x -= C * (S + T)
print(x)