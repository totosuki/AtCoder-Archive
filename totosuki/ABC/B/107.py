H, W = map(int, input().split())
A = []
rslt = []
row_l = []
col_l = []

for i in range(H):
  a = input()
  A.append(a)
  if "#" in a:
    row_l.append(i)

for col in range(W):
  flag = False
  for row in range(H):
    if A[row][col] == "#":
      flag = True
  
  if flag:
    col_l.append(col)

for row in row_l:
  tmp = []
  for col in col_l:
    tmp.append(A[row][col])
  rslt.append(tmp)

[print("".join(r)) for r in rslt]