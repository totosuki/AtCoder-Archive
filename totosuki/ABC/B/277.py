N = int(input())
S = [input() for _ in range(N)]
i1_check = "HDCS"
i2_check = "A23456789TJQK"
collect = 0

#check1,2
for s in S:
  if s[0] not in i1_check or s[1] not in i2_check:
    break
else:
  collect += 1

#check3
for i in range(len(S)):
  flag = False
  for j in range(len(S)):
    if i == j:continue
    if S[i] == S[j]:
      flag = True
  if flag:
    break
else:
  collect += 1

if collect == 2:
  print("Yes")
else:
  print("No")