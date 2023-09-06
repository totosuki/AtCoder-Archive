s = int(input())
se = set()
a = s
i = 1

while True:
  if a in se:
    print(i)
    break
  else:
    se.add(a)
    if a % 2 == 0:
      a = a // 2
    else:
      a = 3*a + 1
    i += 1