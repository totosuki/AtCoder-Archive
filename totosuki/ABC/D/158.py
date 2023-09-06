from collections import deque

S = deque(list(input()))
Q = int(input())
flag = False

for _ in range(Q):
  T, *arg = input().split()
  T = int(T)

  if T == 1:
    flag = False if flag else True
  else:
    F, C = arg
    F = int(F)
    if F == 1:
      if flag:
        S.append(C)
      else:
        S.appendleft(C)
    else:
      if flag:
        S.appendleft(C)
      else:
        S.append(C)

if flag:
  S.reverse()

print("".join(S))