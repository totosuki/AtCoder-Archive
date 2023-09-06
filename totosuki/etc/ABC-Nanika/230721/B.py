S = input()
cnt = 0

if len(S) != 8:
  print("No")
  exit()

upper_cnt = 0
if S[0].isupper():
  cnt += 1

for s in S[1:-1]:
  if s.isupper():
    break
else:
  if 100000 <= int(S[1:-1]) <= 999999:
    cnt += 1

if S[-1].isupper():
  cnt +=1 

print("Yes") if cnt == 3 else print("No")