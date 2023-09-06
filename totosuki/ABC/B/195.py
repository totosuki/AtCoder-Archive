import sys
input = sys.stdin.buffer.readline

A, B, W = map(int, input().split())
W *= 1000
min_cnt = 0
min_n = max_n = 0

for n in range(1, W+1):
  if A*n <= W <= B*n:
    min_n = n
    break
else:
  print("UNSATISFIABLE")
  exit()

for n in reversed(range(1, W+1)):
  if A*n <= W <= B*n:
    max_n = n
    break

print(min_n ,max_n)