from decimal import Decimal
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
cnt = 0
answer = -1
alcohol = 0

for i in range(N):
  V, P = map(Decimal, input().split())
  alcohol += V * (P / 100)  
  cnt += 1
  if alcohol > X:
    answer = cnt
    break

print(answer)