from collections import defaultdict

N, M = map(int, input().split())
ans = defaultdict(lambda: -1)

for _ in range(N):
    c, s = map(int, input().split())
    ans[c] = max(ans[c], s)

for c in range(1, M+1):
    print(ans[c], end=" ")
