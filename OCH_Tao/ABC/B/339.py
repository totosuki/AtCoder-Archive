H,W,N = map(int,input().split())
l = [["."]*W for i in range(H)]
x = 0
y = 0
f = 0
for i in range(N):
  if l[x][y]==".":
    l[x][y]="#"
    f += 1
  else:
    l[x][y]="."
    f -= 1
  f %= 4
  if f == 0:
    x -= 1
    x %= H
  elif f == 1:
    y += 1
    y %= W
  elif f == 2:
    x += 1
    x %= H
  else:
    y -= 1
    y %= W
for i in range(H):
  print("".join(l[i]))