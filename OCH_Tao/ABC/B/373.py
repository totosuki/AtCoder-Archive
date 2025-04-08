STR = list("BCDEFGHIJKLMNOPQRSTUVWXYZ")
cnt = 0
S = input()
tmp = S.index("A")
for i in STR:
  cnt += abs(tmp-S.index(i))
  tmp = S.index(i)
print(cnt)
