N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = sorted(A+B)
reach = False
for i in C:
  if i in A:
    if reach:
      print("Yes")
      break
    else:
      reach = True
  else:
    reach=False
else:
  print("No")