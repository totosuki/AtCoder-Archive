S = input()
S_set = set(S)
for s in S_set:
  if S.count(s) != 2:
    print("No")
    exit()
print("Yes")