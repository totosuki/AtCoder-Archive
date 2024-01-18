A,B,C = map(int,input().split())
if A > B:
  print("Takahashi")
elif B > A:
  print("Aoki")
elif A == B and C == 1:
  print("Takahashi")
else:
  print("Aoki")