N,T = map(int,input().split())
cnt = []
for i in range(N):
  c,t = map(int,input().split())
  if t<=T:
    cnt.append(c)
try:
  print(min(cnt))
except ValueError:
  print("TLE")