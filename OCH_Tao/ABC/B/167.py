A,B,C,K = map(int,input().split())
cnt = 0
cnt+=min(A,K)
K=max(0,K-A)
K=max(0,K-B)
cnt-=min(C,K)
K=max(0,K-C)
print(cnt)