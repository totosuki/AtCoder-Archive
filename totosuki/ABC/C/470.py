N, Q = map(int, input().split())
now = [0] * (N+1)
X = set()
ans = 0

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        x = q[1]
        X |= {x}
        ans ^= now[x]
        ans ^= now[x]+1
        now[x] += 1
    else:
        tmp = 0
        tmp2 = set()
        for i in X:
            now[i] -= 1
            tmp ^= now[i]
            if now[i] == 0:
                tmp2 |= {i}
        X -= tmp2
        ans = tmp

    print(ans)
