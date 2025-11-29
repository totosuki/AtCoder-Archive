from collections import defaultdict

N = int(input())
a = [[0]*2005 for _ in range(2005)]
b = [[0]*2005 for _ in range(2005)]
zero = 0
ans = defaultdict(int)

for kind in range(1, N+1):
    u, d, l, r = map(int, input().split())
    d += 1
    r += 1
    a[u][l] += 1
    a[u][r] -= 1
    a[d][l] -=1
    a[d][r] += 1
    b[u][l] += kind
    b[u][r] -= kind
    b[d][l] -= kind
    b[d][r] += kind

for i in range(2005):
    for j in range(2005):
        a[i][j] += a[i][j-1]
        b[i][j] += b[i][j-1]

for i in range(2005):
    for j in range(2005):
        a[i][j] += a[i-1][j]
        b[i][j] += b[i-1][j]

for i in range(1, 2001):
    for j in range(1, 2001):
        zero += a[i][j] == 0
        if a[i][j] == 1:
            ans[b[i][j]] += 1

for kind in range(1, N+1):
    print(zero + ans[kind])
