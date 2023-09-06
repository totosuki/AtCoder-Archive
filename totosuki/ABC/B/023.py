N = int(input())
S = input()
rslt = "b"

for i in range(N // 2):
  if i % 3 == 0:
    rslt = "a" + rslt + "c"
  elif i % 3 == 1:
    rslt = "c" + rslt + "a"
  elif i % 3 == 2:
    rslt = "b" + rslt + "b"

if rslt == S:
  print(N // 2)
else:
  print(-1)