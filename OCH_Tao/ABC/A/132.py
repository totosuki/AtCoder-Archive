S = input()
x = sorted(S)
if x[0]==x[1]==x[2]==x[3]:
  print("No")
elif x[0]==x[1] and x[2]==x[3]:
  print("Yes")
else:
  print("No")