H,W = map(int,input().split())
R,C = map(int,input().split())
cnt = 0
if 0<R-1:
  cnt+=1
if R+1<=H:
  cnt+=1
if 0<C-1:
  cnt+=1
if C+1<=W:
  cnt+=1
print(cnt)