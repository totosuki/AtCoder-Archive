N,K = map(int,input().split())
cnt = 0
for i in range(1,N+1):
    for l in range(1,N+1):
        if 1 <= K - (i+l) <= N:
            cnt += 1
print(cnt)