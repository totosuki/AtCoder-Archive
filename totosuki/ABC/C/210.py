import sys
input = sys.stdin.buffer.readline

from collections import defaultdict

N, K = map(int, input().split())
C = list(map(int, input().split()))

now_c = defaultdict(int)
max_cnt = 0
cnt = 0

for i in range(K):
  now_c[C[i]] += 1
  if now_c[C[i]] == 1:
    max_cnt += 1
    cnt += 1

for i in range(N - K):
  leave_c = C[i]
  add_c = C[i + K]
  
  now_c[leave_c] -= 1
  if now_c[leave_c] == 0:
    cnt -= 1
  
  now_c[add_c] += 1
  if now_c[add_c] == 1:
    cnt += 1
  
  max_cnt = max(cnt, max_cnt)

print(max_cnt)