N = int(input())
T = list(input())
ans = [0,0]
cnt = 0
for i in T:
  if i=="R":
    cnt+=1
  else:
    if cnt%4==0:
      ans[0]+=1
    elif cnt%4==1:
      ans[1]-=1
    elif cnt%4==2:
      ans[0]-=1
    else:
      ans[1]+=1
print(*ans)