S = list(input())
T = input()
for i in range(len(S)):
  X = "".join(S[i:]+S[:i])
  if X==T:
    print("Yes")
    break
else:
  print("No")