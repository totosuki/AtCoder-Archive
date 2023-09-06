import sys
input = sys.stdin.buffer.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))
rslt = [False] * N

i = X
cnt = 0
while True:
  if rslt[i-1] == False:
    rslt[i-1] = True
    i = A[i-1]
    cnt += 1
  else:
    break

print(cnt)