N = int(input())
rslt = 1000 - N % 1000
if rslt == 1000:
  print(0)
else:
  print(rslt)