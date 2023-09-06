N = input()

if len(N) <= 1:
  print(0)
  exit()

check_maxnum = int(N[:len(N)//2])
rslt = 0
if len(N) % 2 == 0:
  for i in range(check_maxnum + 1):
    if "0" in str(i)[0]:
      continue
    else:
      text = str(i) + str(i)
      if int(text) <= int(N):
        rslt += 1
else:
  for i in range(check_maxnum * 10 + 1):
    if "0" in str(i)[0]:
      continue
    else:
      text = str(i) + str(i)
      if int(text) <= int(N):
        rslt += 1
print(rslt)