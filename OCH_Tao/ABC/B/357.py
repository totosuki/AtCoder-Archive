S = input()
U = 0
L = 0
for i in list(S):
  if i.isupper():
    U+=1
  else:
    L+=1
print(S.upper() if U>L else S.lower())