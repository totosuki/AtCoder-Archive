cols = [[]*9 for _ in range(9)]
tile = []
group_33 = [[] * 9 for _ in range(9)]

for _ in range(9):
  A = list(map(int, input().split()))
  for i in range(9):
    cols[i].append(A[i])
  tile.append(A)

# 条件1と2を満たすかどうか
for i in range(9):
  col_se = set(cols[i])
  row_se = set(tile[i])
  if len(col_se) == 9 and len(row_se) == 9:
    continue
  else:
    print("No")
    exit()

for row in range(9):
  for col in range(9):
    if row <= 2:
      if col <= 2:
        group_33[0].append(tile[row][col])
      elif col <= 5:
        group_33[1].append(tile[row][col])
      else:
        group_33[2].append(tile[row][col])
    elif row <= 5:
      if col <= 2:
        group_33[3].append(tile[row][col])
      elif col <= 5:
        group_33[4].append(tile[row][col])
      else:
        group_33[5].append(tile[row][col])
    else:
      if col <= 2:
        group_33[6].append(tile[row][col])
      elif col <= 5:
        group_33[7].append(tile[row][col])
      else:
        group_33[8].append(tile[row][col])

# 条件3を満たすかどうか
for i in range(9):
  group_se = set(group_33[i])
  if len(group_se) == 9:
    continue
  else:
    print("No")
    exit()

print("Yes")