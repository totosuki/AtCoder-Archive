import sys; from collections import defaultdict
input = sys.stdin.buffer.readline

sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
  A, B = map(lambda x: int(x) - 1, input().split())
  graph[A].append(B)
  graph[B].append(A)

ok = [False] * (N)

def dfs(now: int):
  ok[now] = True
  for ne in graph[now]:
    if ok[ne] == False:
      dfs(ne)
  return
dfs(0)

print("The graph is not connected.") if False in ok else print("The graph is connected.")