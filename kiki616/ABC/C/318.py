N,D,P = map(int,input().split())
F = list(map(int,input().split()))
F.sort()
memo = 0
cost = 0
isis = False
for i in range(N):
    if F[i] > P/D:
        memo = i
        isis = True
        break
    cost = cost + F[i]
if isis:
    cnt = (N - memo) % D
    cnt_ = 0
    if cnt == 0:
        cost = cost + P*(N - memo //D)
    else:
        for i in range(memo,memo+cnt):
            cnt_ = cnt_ + F[i]
        if cnt_ > P:
            cost = cost + P*((N - memo) //D + 1)
        else:
            cost = cost + P*((N - memo) //D) + cnt_
print(cost)