N = int(input())
S = input()
x = 0
rslt = 0
for s in S:
  if s == "I":
    x += 1
  else:
    x -= 1
  rslt = max(x, rslt)

print(rslt)