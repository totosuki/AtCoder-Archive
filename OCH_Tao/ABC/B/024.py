N,T = map(int,input().split())
time = None
cnt = 0
for i in range(N):
  a = (int(input()))
  if not time:
    time = a+T
  else:
    if a > time:
      cnt += T
      time = a+T
    else:
      cnt += T-(time-a)
      time = a+T
else:
  cnt += T
print(cnt)