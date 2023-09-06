H, W = map(int, input().split())
data = [input() for _ in range(H)]
a,b,c,d = [],[],[],[]
phase = 0

#find_a
for row in range(H):
  for col in range(W):
    if data[row][col] == "#":
      a = [row,col]
      phase = 1
      break
  if phase == 1:
    break

#find_b
for col in reversed(range(0, W)):
  if data[a[0]][col] == "#":
    b = [a[0], col]
    phase = 2
    break

#find_c
for row in reversed(range(H)):
  for col in range(W):
    if data[row][col] == "#":
      c = [row, col]
      phase = 3
      break
  if phase == 3:
    break

#find_d
for col in reversed(range(0,W)):
  if data[c[0]][col] == "#":
    d = [c[0], col]
    phase = 4
    break

# print(a, b, c, d)

if a[1] != c[1]:
  if a[1] > c[1]:
    print(a[0]+1, c[1]+1)
  else:
    print(c[0]+1, a[1]+1)
  exit()
elif b[1] != d[1]:
  if b[1] < d[1]:
    print(b[0]+1, d[1]+1)
  else:
    print(d[0]+1, b[1]+1)
  exit()

for row in range(a[0],c[0]+1):
  for col in range(a[1], b[1]+1):
    if data[row][col] == ".":
      print(row+1, col+1)