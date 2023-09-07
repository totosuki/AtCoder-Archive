N,M,P = map(int,input().split())
print((N-M)//P+1 if (N-M) >= 0 else 0)