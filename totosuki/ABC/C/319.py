import sys; from itertools import permutations
input = sys.stdin.buffer.readline

C = [list(map(int, input().split())) for _ in range(3)]

angles = ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2))
s_angles = [((0,0),(0,1),(0,2)),
            ((1,0),(1,1),(1,2)),
            ((2,0),(2,1),(2,2)),
            ((0,0),(1,0),(2,0)),
            ((0,1),(1,1),(2,1)),
            ((0,2),(1,2),(2,2)),
            ((0,0),(1,1),(2,2)),
            ((0,2),(1,1),(2,0))]

permutation = permutations(angles)
all_cnt = 0
cnt = 0

for perm in permutation:
  all_cnt += 1
  flag = True
  for s_angle in s_angles:
    ya, xa = s_angle[0]
    yb, xb = s_angle[1]
    yc, xc = s_angle[2]
    
    if C[ya][xa] == C[yb][xb]:
      ia = perm.index(s_angle[0])
      ib = perm.index(s_angle[1])
      ic = perm.index(s_angle[2])
      if ia < ic and ib < ic:
        flag = False
        break
    if C[yb][xb] == C[yc][xc]:
      ia = perm.index(s_angle[0])
      ib = perm.index(s_angle[1])
      ic = perm.index(s_angle[2])
      if ib < ia and ic < ia:
        flag = False
        break
    if C[ya][xa] == C[yc][xc]:
      ia = perm.index(s_angle[0])
      ib = perm.index(s_angle[1])
      ic = perm.index(s_angle[2])
      if ia < ib and ic < ib: 
        flag = False
        break
  if flag:
    cnt += 1

print(cnt / all_cnt)