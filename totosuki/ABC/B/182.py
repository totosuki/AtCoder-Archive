import sys
input = sys.stdin.buffer.readline

N = int(input())  
A = list(map(int, input().split()))

rslt = -1
mx = 0

for x in range(2, 1001):
  sm = sum(a % x == 0 for a in A)
  if mx < sm:
    mx = sm
    rslt = x

print(rslt)