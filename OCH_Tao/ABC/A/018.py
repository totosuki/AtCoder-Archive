l = []
i = 3
while i > 0:
  l.append(int(input()))
  i -= 1

l_sorted = sorted(l,reverse=True)

while i < 3:
  print(l_sorted.index(l[i]) + 1)
  i += 1