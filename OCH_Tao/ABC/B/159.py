S = input()
N = len(S)
if S==S[::-1]:
  if (X:=S[:(N-1)//2])==X[::-1]:
    if (Y:=S[(N+3)//2-1:])==Y[::-1]:
      print("Yes")
    else:
      print("No")
  else:
    print("No")
else:
  print("No")