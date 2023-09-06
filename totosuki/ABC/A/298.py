N = int(input())
S = input()
flag1 = False
flag2 = False
for s in S:
  if s == "o":
    flag1 = True
  if s == "x":
    flag2 = True
if flag1 == True and flag2 == False:
  print("Yes")
else:
  print("No")