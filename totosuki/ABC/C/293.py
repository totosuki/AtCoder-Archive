import sys, itertools
input = sys.stdin.buffer.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
data = [i for i in range(H + W - 2)]
cnt = 0

for comb in itertools.combinations(data, H-1):
  now_h = now_w = 0
  se = {A[now_h][now_w]}
  for i in range(H + W - 2):
    if i in comb:
      now_h += 1
    else:
      now_w += 1
    se.add(A[now_h][now_w])
  
  if len(se) == H + W - 1:
    cnt += 1

print(cnt)