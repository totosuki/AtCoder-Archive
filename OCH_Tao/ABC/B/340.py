Q = int(input())
a = []
for i in range(Q):
  x,y = map(int,input().split())
  if x == 1:
    a.append(y)
  else:
    print(a[-y])