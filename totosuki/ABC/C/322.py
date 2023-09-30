import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(M):
  day = A[i]
  li = []
  
  if i == 0: # 1日目までやる
    while day != 0:
      li.append(A[i] - day)
      day -= 1
    print(*reversed(li), sep = "\n")
  else:
    while day != A[i-1]:
      li.append(A[i] - day)
      day -= 1
    print(*reversed(li), sep = "\n")