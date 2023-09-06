import sys; from collections import defaultdict, deque
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
S = input().decode().rstrip()
C = list(map(int, input().split()))
data = defaultdict(deque)
rslt = []

for s, c in zip(S, C):
  data[c].append(s)

for c in data.keys():
  data[c].rotate()

# solve
for c in C:
  rslt.append(data[c].popleft())

print("".join(rslt))