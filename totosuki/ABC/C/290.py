import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = sorted(set(map(int, input().split())))
max_mex = 0
for a in A:
  if a == max_mex:
    max_mex += 1
  else:
    break

max_mex = min(max_mex, K)

print(max_mex)