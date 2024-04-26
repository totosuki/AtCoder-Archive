H,W,N = map(int,input().split())
T = list(input())
S = []
for i in range(H):
  S.append(list(input()))
cnt = 0
for i in range(1,H-1):
  for j in range(1,W-1):
    if S[i][j]=="#":
      continue
    now = [i,j]
    for k in T:
      if k=="L":
        now[1]-=1
      elif k=="R":
        now[1]+=1
      elif k=="U":
        now[0]-=1
      else:
        now[0]+=1
      if S[now[0]][now[1]]=="#":
        break
    else:
      cnt+=1
print(cnt)