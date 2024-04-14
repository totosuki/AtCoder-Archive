S = list(input())
set_S = set(S)

ans = "Yes"

for i in range(105):
  cnt = 0
  for s in set_S:
    if S.count(s) == i:
      cnt += 1
  if cnt == 0 or cnt == 2:
    continue
  else:
    ans = "No"
    break

print(ans)