# 未AC
N,A,B = map(int,input().split())
D = list(map(int,input().split()))
mod = list(map(lambda x: x%(A+B),D))
if max(mod)-min(mod)<A:
  print("Yes")
else:
  print("No")