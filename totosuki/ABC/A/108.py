K = int(input())
if K % 2:
  rslt = (K//2) * (K//2 + 1)
  print(rslt)
else:
  rslt = (K//2) * (K//2)
  print(rslt)