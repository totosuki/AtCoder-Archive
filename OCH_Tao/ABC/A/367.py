A,B,C = map(int,input().split())
if B<=A<=C or (B>C and (B<=A or A<=C)):
  print("No")
else:
  print("Yes")