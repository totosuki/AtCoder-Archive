from collections import deque

N = int(input())
A = list(map(int, input().split()))

l = deque()
i = 0
while True:
  l.append(A[i])
  while True:
    if len(l) == 1:
      break
    if l[-1] != l[-2]:
      break
    x = l.pop()
    y = l.pop()
    l.append(x+1)
  i += 1
  if i == N:
    break

print(len(l))