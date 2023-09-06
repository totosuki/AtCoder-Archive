import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

left = -1
right = 10**9+5

while (right - left) > 1:
  mid = (right + left) // 2
  buy_cnt = 0
  sell_cnt = 0
  
  for i in range(N):
    if A[i] <= mid:
      buy_cnt += 1
  for i in range(M):
    if B[i] >= mid:
      sell_cnt += 1
  
  if buy_cnt >= sell_cnt:
    right = mid
  else:
    left = mid

print(right)

"""
x x x x o o o o
      ^ ^
      l r
だからrをoutput
"""