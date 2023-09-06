import sys, itertools
input = sys.stdin.buffer.readline

N, W = map(int, input().split())
A = list(map(int, input().split()))
se = set()

for i in range(1, min(3, len(A))+1):
  for combo in itertools.combinations(A, i):
    tmp = sum(combo)
    if tmp <= W:
      se.add(tmp)

print(len(se))