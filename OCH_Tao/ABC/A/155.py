A,B,C = map(int,input().split())
if A == B and C != A:
  print('Yes')
elif B == C and A != B:
  print('Yes')
elif C == A and B != C:
  print('Yes')
else:
  print('No')