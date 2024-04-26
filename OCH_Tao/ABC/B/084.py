A,B = map(int,input().split())
S = list(input())
x = S.pop(A)
if x == "-":
  if ("".join(S)).isdecimal():
    print("Yes")
  else:
    print("No")
else:
  print("No")