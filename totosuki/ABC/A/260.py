S = input()
flag = False
for i in range(3):
  if S.count(S[i]) == 1:
    print(S[i])
    exit()

if not flag:
  print(-1)