from collections import defaultdict, deque

N = int(input())
U = []
D = []
L = []
R = []
# [cnt, id]
tile = [[0]*2000 for _ in range(2000)]
cloud = [[0]*2000 for _ in range(2000)]
ans = defaultdict(int)


zero = deque([[i,j] for i in range(2000) for j in range(2000)])
one = deque([])

for kind in range(N):
    u, d, l, r = map(lambda x: int(x)-1, input().split())
    U.append(u)
    D.append(d)
    L.append(l)
    R.append(r)

    x = len(one)
    for _ in range(x):
        i, j = one.popleft()
        if not (u <= i <= d and l <= j <= r):
            one.append([i, j])
        else:
            ans[cloud[i][j]] -= 1
            cloud[i][j] = -1
    
    x = len(zero)
    for _ in range(x):
        i, j = zero.popleft()
        if not (u <= i <= d and l <= j <= r):
            zero.append([i, j])
        else:
            one.append([i, j])
            cloud[i][j] = kind
            ans[kind] += 1

for kind in range(N):
    print(len(zero) + ans[kind])
