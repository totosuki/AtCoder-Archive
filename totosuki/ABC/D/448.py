from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)

N = int(input())
A = list(map(int, input().split()))
G = defaultdict(list)

for _ in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = [False] * N
visited = [False] * N

def dfs(i: int, d: defaultdict, flag: bool):
    val = A[i-1]
    d[val] += 1

    if d[val] == 2 or flag:
        ans[i-1] = True
        flag = True

    visited[i-1] = True

    for next in G[i]:
        if not visited[next-1]:
            x = dfs(next, d, flag)
            d[x] -= 1
    
    return val

dfs(1, defaultdict(int), False)

for a in ans:
    print("Yes" if a else "No")
