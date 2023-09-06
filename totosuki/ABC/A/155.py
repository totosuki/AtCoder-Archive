A, B, C = map(int, input().split())
if A == B and B != C or  B == C and A != C or C == A and A != B:
  print("Yes")
else:
  print("No")