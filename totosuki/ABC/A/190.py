A, B, C = map(int, input().split())
if A > B:
  print("Takahashi")
elif A < B:
  print("Aoki")
else:
  if C == 0:
    print("Aoki")
  else:
    print("Takahashi")