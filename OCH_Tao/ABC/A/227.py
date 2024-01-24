N,K,A = map(int,input().split())
x = K%N+A-1
if 0 < x <= N:
  print(x)
elif x <= 0:
  print(x+N)
else:
  print(x-N)