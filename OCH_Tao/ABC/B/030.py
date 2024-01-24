from math import degrees,pi
n,m = map(int,input().split())
n = n%12
l = []
l.append(degrees((m/30)*pi))
l.append(degrees((n/6)*pi+(m/360)*pi))
l.sort(reverse=True)
x = l[0]-l[1]
if x <= 180:
  print(x)
else:
  print(360-x)