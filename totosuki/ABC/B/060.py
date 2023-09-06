import time
st = time.time()
A, B, C = map(int, input().split())
x = A
n = 1
while True:
  nt = time.time()
  if nt - st <= 1.92:
    if x % B == C:
      print("YES")
      break
  else:
    print("NO")
    break
  
  n += 1
  x = A * n