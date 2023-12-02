N,K = map(int,input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
isis = 0
for i in range(N):
    if K - P[i] in Q:
        isis = 1
print("Yes"if isis else"No")