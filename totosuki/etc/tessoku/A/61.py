import sys; from collections import defaultdict
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

for k in range(1, N+1):
  print(f"{k}:", end = " {")
  print(*graph[k], sep = ", ", end = "")
  print("}")
