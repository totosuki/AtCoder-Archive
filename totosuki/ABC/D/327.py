from collections import defaultdict
import sys

sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

X = [-1] * (N+1)
graph = defaultdict(list)
answer = "Yes"

for i in range(M):
  graph[A[i]].append(B[i])
  graph[B[i]].append(A[i])

# print(graph)

def dfs(id, c):
  # print(f"id : {id}, c : {c}")
  
  X[id] = c
  
  # print(f"X : {X}")
  
  for next in graph[id]:
    # print(f"next : {next}")
    if X[next] == c:
      # print("Return False")
      return False
    if X[next] == -1 and not dfs(next, 1 - c):
      return False
  
  return True

for i in range(1, N+1):
  if X[i] == -1:
    if dfs(id = i, c = 0) == False:
      answer = "No"

print(answer)