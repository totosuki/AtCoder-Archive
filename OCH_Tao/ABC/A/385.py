A, B, C = map(int, input().split())
if A == B == C or A+B == C or B+C == A or C+A == B:
  print("Yes")
else:
  print("No")
