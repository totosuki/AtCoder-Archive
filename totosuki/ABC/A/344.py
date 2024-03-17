S = input()
ans = ""
cnt = 0
for s in S:
  if s == "|":
    cnt += 1
  else:
    if cnt == 0 or cnt == 2:
      ans += s
print(ans)