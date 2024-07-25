S = input()
if len(S)>1:
  print("Yes" if S[::2].islower() and S[1::2].isupper() else "No")
else:
  print("Yes" if S.islower() else "No")