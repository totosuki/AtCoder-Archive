X = int(input())
cnt = 0
rslt = 0
plus = 0.00005

if int(X) % 100 == 0:
  X += 1
  cnt += 1
  rslt = 1

while True:
  if cnt == 20000:
    cnt = 0
    rslt += 1

  if int(X) % 100 == 0:
    print(rslt)
    break
  else:
    X += plus
    cnt += 1