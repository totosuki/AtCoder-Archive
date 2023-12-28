A,B,C,D = map(int,input().split())
L = A+B
R = C+D
if L == R:
  print("Balanced")
elif L > R:
  print("Left")
else:
  print("Right")