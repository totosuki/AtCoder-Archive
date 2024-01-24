S = input()
if S[0]==S[1]==S[2]:
  print(1)
elif S[0]!=S[1] and S[1]!=S[2] and S[2]!=S[0]:
  print(6)
else:
  print(3)