N = input()
fx = sum(list(map(int,list(N))))
if int(N)%fx==0:
  print("Yes")
else:
  print("No")