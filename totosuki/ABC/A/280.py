H, W = map(int, input().split())
rslt = 0
for _ in range(H):
  text = input()
  for t in text:
    if t == "#":
      rslt += 1
print(rslt)