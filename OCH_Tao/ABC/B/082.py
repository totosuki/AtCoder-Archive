S = list(input())
T = list(input())
S.sort()
T.sort(reverse=True)
if "".join(S)<"".join(T):
  print("Yes")
else:
  print("No")