N = int(input())
L = 0
R = 50*int(1e6)
while L < R:
  M = (L+R)//2
  if N <= (M/1e6)**3+(M/1e6):
    R = M
  else:
    L = M+1
print(L/1e6)
