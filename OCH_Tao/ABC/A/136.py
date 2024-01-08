A,B,C = map(int,input().split())
x = C-(A-B)
if x < 0:
  print(0)
else:
  print(x)