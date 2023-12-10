from itertools import permutations
from copy import deepcopy

def return_permutations(H, W):
  l = []
  for i in range(H-1):
    l.append(("H", i))
  for i in range(W-1):
    l.append(("W", i))
  return permutations(l)

def solve(H, W, A: list, B: list):
  rslt = 1 << 60
  for perm in return_permutations(H, W):
    L = deepcopy(A)
    cnt = 0
    for p in perm:
      c, i = p
      cnt += 1
      if c == "H":
        L[i], L[i+1] = L[i+1], L[i]
      else:
        for j in range(H):
          L[j][i], L[j][i+1] = L[j][i+1], L[j][i]
      flag = True
      for i in range(H):
        for j in range(W):
          if L[i][j] != B[i][j]:
            flag = False
      if flag:
        rslt = min(rslt, cnt)
        break
  
  flag = True
  for k in range(H):
    for l in range(W):
      if A[k][l] != B[k][l]:
        flag = False
  if flag:
    print(0)
  elif rslt == 1 << 60:
    print(-1)
  else:
    print(rslt)

def main():
  H, W = map(int, input().split())
  A = [list(map(int, input().split())) for _ in range(H)]
  B = [list(map(int, input().split())) for _ in range(H)]
  solve(H, W, A, B)

main()