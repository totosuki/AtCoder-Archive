S = list(input())
T = int(input())
x = 0
y = 0
cnt = 0
for i in S:
  if i == "L":
    x -= 1
  elif i == "R":
    x += 1
  elif i == "U":
    y += 1
  elif i == "D":
    y -= 1
  else:
    cnt += 1
N = abs(x)+abs(y)
if T == 1:
  print(N+cnt)
else:
  if N>cnt:
    print(N-cnt)
  else:
    while cnt > 0:
      if N>0:
        N -= 1
        cnt -= 1
      else:
        N += 1
        cnt -= 1
    else:
      print(N)