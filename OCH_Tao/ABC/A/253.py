A,B,C = map(int,input().split())
l = [A,B,C]
l.sort()
if l[1]==B:
  print("Yes")
else:
  print("No")