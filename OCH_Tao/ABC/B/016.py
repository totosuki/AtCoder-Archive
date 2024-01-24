A,B,C = map(int,input().split())
if C == A+B and C == A-B:
  print("?")
elif C == A+B:
  print("+")
elif C == A-B:
  print("-")
else:
  print("!")