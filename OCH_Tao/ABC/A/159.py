N,M = map(int,input().split())

if N > 0:
  x = (N*(N-1))//2
else:
  x = 0

if M > 0:
  y = (M*(M-1))//2
else:
  y = 0

print(x+y)